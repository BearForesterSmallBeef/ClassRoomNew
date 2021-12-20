import os
import sys
import pygame

pygame.init()
pygame.key.set_repeat(200, 70)
FPS = 50
WIDTH = 400
HEIGHT = 300
STEP = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Заставка",
                  "",
                  "Правила игры",
                  "Если в правилах несколько строк",
                  "приходится выводить из построчно"]
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 60
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = 10
        screen.blit(string_rendered, intro_rect)
        text_coord += intro_rect.height + 10  # расстояние между строками

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
            pygame.display.flip()
            clock.tick(FPS)


start_screen()


def load_level(filename):
    filename = "data/" + filename
    with open(filename, "r") as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, "."), level_map))


tile_images = {
    'wall': load_image("box.png"),
    'empty': load_image("grass.png"),
}
player_image = load_image("mario.png")
STEP = tile_width = title_height = 50


class Title(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, title_height * pos_y
        )


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, title_height * pos_y + 5
        )


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == ".":
                Title("empty", x, y)
            elif level[y][x] == "#":
                g = Title("wall", x, y)
                g.add(box_group)
            elif level[y][x] == "@":
                Title("empty", x, y)
                new_player = Player(x, y)
    return new_player, x, y


player, level_x, level_y = generate_level(load_level("levelex.txt"))
print(box_group)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


camera = Camera()


# Главный Игровой цикл
running = True
while running:
    WIDTH, HEIGHT = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= STEP
                if pygame.sprite.spritecollide(player, box_group, False):
                    player.rect.x += STEP
            if event.key == pygame.K_RIGHT:
                player.rect.x += STEP
                if pygame.sprite.spritecollide(player, box_group, False):
                    player.rect.x -= STEP
            if event.key == pygame.K_UP:
                player.rect.y -= STEP
                if pygame.sprite.spritecollide(player, box_group, False):
                    player.rect.y += STEP
            if event.key == pygame.K_DOWN:
                player.rect.y += STEP
                if pygame.sprite.spritecollide(player, box_group, False):
                    player.rect.y -= STEP

    for sprite in all_sprites:
        camera.apply(sprite)
#    camera.update(player)
    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
