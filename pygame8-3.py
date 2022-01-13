import os
import random
import sys
import pygame
from pygame.locals import RESIZABLE, FULLSCREEN

pygame.init()
FPS = 20
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


sound = pygame.mixer.Sound('data/in.wav')
vol = 1


# Главный Игровой цикл
running = True
while running:
    WIDTH, HEIGHT = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            channel = sound.play()
            sound.set_volume(vol)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            vol = 0.3
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            vol = 1
    screen.fill(pygame.Color(0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
