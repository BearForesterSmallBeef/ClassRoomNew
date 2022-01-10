import os
import sys
import pygame

pygame.init()
FPS = 20

WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
buttons = pygame.sprite.Group()
x, y = 0, 0


def load_image(name, color_key=None, way_to_file="try\\left"):
    fullname = os.path.join(way_to_file, name)
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


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h,
                 imagepath=None, imagename=None,
                 ONtext=None, ONfontsize=30, ONtextcolor=(100, 255, 100),
                 UNDERtext=None, UNDERfontsize=30, UNDERtextcolor=(100, 255, 100)):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.imagepath, self.imagename = imagepath, imagename
        self.ONtext, self.ONfontsize, self.ONtextcolor = ONtext, ONfontsize, ONtextcolor
        self.UNDERtext, self.UNDERfontsize, self.UNDERtextcolor = UNDERtext, UNDERfontsize, UNDERtextcolor

        self.rect = pygame.Rect((0, 0), (self.w, self.h))
        self.rect = self.rect.move(x, y)

        if self.imagepath and self.imagename:
            self.image = load_image(self.imagename, way_to_file=self.imagepath)
            self.image = pygame.transform.scale(self.image, (self.w, self.h))
            self.image = self.image.subsurface(pygame.Rect((0, 0), self.rect.size))

        if self.ONtext:
            self.ONfont = pygame.font.Font(None, self.ONfontsize)
            self.ONrendertext = self.ONfont.render(self.ONtext, True, self.ONtextcolor)
            self.ONw = self.ONrendertext.get_width()
            self.ONh = self.ONrendertext.get_height()
            self.ONx = self.x + self.w // 2 - self.ONw // 2
            self.ONy = self.y + self.h // 2 - self.ONh // 2





class Stoun(pygame.sprite.Sprite):
    image = load_image(f"BigStoun.png", way_to_file="other_pictures")

    def __init__(self, x, y, a):
        super().__init__(all_sprites)
        self.x, self.y, self.w, self.h = x, y, a, a
        self.image = Stoun.image
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = pygame.Rect((0, 0), (self.w, self.h))
        self.rect = self.rect.move(x, y)
        self.image = self.image.subsurface(pygame.Rect((0, 0), self.rect.size))

    def update(self):
        pass


stoun = Stoun(290, 300, 150)


running = True
while running:
    WIDTH, HEIGHT = pygame.display.get_window_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
    screen.fill(pygame.Color("pink"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)