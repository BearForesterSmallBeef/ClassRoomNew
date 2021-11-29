import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, hight = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Движущийся шар")
    running = True
    x_pos, k = 0, 1

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
        x_pos += k
        if x_pos > width:
            k *= -1
        pygame.display.flip()
    pygame.quit()
