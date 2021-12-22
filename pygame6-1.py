import os
import sys
import pygame
import random


flag = False
t = pygame.time.get_ticks()
pygame.init()
size = width, hight = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()


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


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)

    def update(self):
        d = True
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
            d = False
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
            d = False
        if d:
            other = pygame.sprite.spritecollide(self, all_sprites, False)
            for i in other:
                if flag and not vertical_borders.has(i) and not horizontal_borders.has(i):
                    self.vy, i.vy = i.vy, self.vy
                    self.vx, i.vx = i.vx, self.vx
        if self.rect.x <= 5:
            self.rect = self.rect.move((6 - self.rect.x), 0)
        elif self.rect.x >= width - 5:
            self.rect = self.rect.move(self.rect.x - width + 4, 0)
        if self.rect.y <= 5:
            self.rect = self.rect.move(0, 6 - self.rect.y)
        elif self.rect.y >= hight - 5:
            self.rect = self.rect.move(0, self.rect.y - hight + 4)


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - 1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def main():
    global flag

    pygame.display.set_caption("Шаблон")
    clock = pygame.time.Clock()

    Border(5, 5, width - 5, 5)
    Border(5, hight - 5, width - 5, hight - 5)
    Border(5, 5, 5, hight - 5)
    Border(width - 5, 5, width - 5, hight - 5)

    for i in range(200):
        Ball(9, 200, 200)

    running = True
    while running:
        if t < pygame.time.get_ticks() - 1000:
            flag = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(24)
    pygame.quit()


if __name__ == '__main__':
    main()
