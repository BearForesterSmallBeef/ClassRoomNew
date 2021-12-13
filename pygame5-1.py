import os
import sys
import pygame


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


def main():
    pygame.init()
    size = width, hight = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Шаблон")
    screen.fill("white")
    image = load_image('Робот.png', -1)
    image1 = pygame.transform.scale(image, (200, 100))
    image2 = pygame.transform.scale(image, (100, 200))
    image3 = pygame.transform.scale(image, (200, 200))
    screen.blit(image1, (100, 200))
    screen.blit(image2, (100, 250))
    screen.blit(image3, (200, 200))
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(image, event.pos)

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
