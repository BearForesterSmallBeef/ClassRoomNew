import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, hight = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Белый кролик")
    running = True
    clock = pygame.time.Clock()

    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 1000)

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, "white", event.pos, 20)
                pygame.draw.ellipse(screen, "white", (event.pos[0] - 15, event.pos[1] - 40, 10, 40))
                pygame.draw.ellipse(screen, "white", (event.pos[0] + 5, event.pos[1] - 40, 10, 40))
            if event.type == MYEVENTTYPE:
                print("Мое событие сработало")

        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
