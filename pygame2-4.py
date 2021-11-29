import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, hight = 800, 400
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    x1, y1 = 0, 0
    w, h = 0, 0
    drawing = False
    pygame.display.set_caption("Движущийся шар")
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x1, y1 = event.pos
                w, h = 0, 0
            if event.type == pygame.MOUSEBUTTONUP and drawing:
                screen2.blit(screen, (0, 0))
                drawing = False

            if event.type == pygame.MOUSEMOTION:
                w, h = event.pos[0] - x1, event.pos[1] - y1

        screen.fill((0, 0, 0))
        screen.blit(screen2, (0, 0))
        if drawing and h and w:
            pygame.draw.rect(screen, (0, 255, 0), (x1, y1, w, h), 1, 0)
        pygame.display.flip()
    pygame.quit()
