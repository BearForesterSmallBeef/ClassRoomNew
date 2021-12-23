import os
import random
import sys
import pygame
from pygame.locals import RESIZABLE, FULLSCREEN

pygame.init()
FPS = 20
gravity = 0.20
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
pygame.mouse.set_visible(0)


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


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocuty = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = gravity

    def update(self):
        self.velocuty[1] += self.gravity
        self.rect.x += self.velocuty[0]
        self.rect.y += self.velocuty[1]
        screen_rect = (0, 0, WIDTH, HEIGHT)
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position, particles_count=20, numbers=range(-5, 6)):
    for i in range(particles_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


# Главный Игровой цикл
running = True
while running:
    WIDTH, HEIGHT = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_particles(pygame.mouse.get_pos())
    screen.fill(pygame.Color(0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)