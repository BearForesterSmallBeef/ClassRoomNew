import pygame
from random import random, randint

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("ТЕЛЕВИЗОР")
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for i in range(10000):
            screen.fill(pygame.Color("white"), (random() * width, random() * height, randint(1, 3), randint(1, 3)))

        pygame.display.flip()
    pygame.quit()
