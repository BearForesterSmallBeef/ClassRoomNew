import os
import random
import sys
import pygame


pygame.init()
size = width, hight = 600, 300
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image('bomb.png')
    image_boom = load_image('boom.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - 51)
        self.rect.y = random.randrange(hight - 50)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Бомбы")
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    n = 20
    for i in range(n):
        Bomb(all_sprites)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        screen.fill("black")
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
