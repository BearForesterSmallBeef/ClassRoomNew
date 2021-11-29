import pygame
from random import random


if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    for i in range(10000):
        screen.fill(pygame.Color("white"), (random() * width, random() * height, 1, 1))

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
