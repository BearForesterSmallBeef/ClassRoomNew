import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, hight = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Движущийся шар")
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    pygame.quit()
