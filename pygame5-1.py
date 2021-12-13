import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def main():
    pygame.init()
    size = width, hight = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Шаблон")
    screen.fill("white")
    image = load_image('')
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
