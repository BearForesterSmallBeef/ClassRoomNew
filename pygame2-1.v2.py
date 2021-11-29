import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, hight = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Движущийся шар")
    running = True
    x_pos, k = 0, 1
    v = 300
    fps = 30
    clock = pygame.time.Clock()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (x_pos + 20, 200), 20)
        x_pos += v / fps * k
        clock.tick(fps)
        if x_pos > width - 30 or x_pos < 0:
            k *= -1
        pygame.display.flip()
    pygame.quit()
