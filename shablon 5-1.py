import os
import sys
import pygame


pygame.init()
size = width, hight = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


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
    pygame.display.set_caption("Шаблон")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()