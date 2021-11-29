import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, hight = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Белый кролик")
    running = True
    drawing = False
    s = 0
    clock = pygame.time.Clock()
    x1, y1 = 0, 0

    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 1)

    while running:
        screen.fill("yellow")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                drawing = True
                s = 0
            if event.type == MYEVENTTYPE:
                if drawing:
                    s += 1

        screen.fill("blue")
        pygame.draw.circle(screen, "yellow", (x1, y1), s)
        pygame.display.flip()
        print(clock.get_fps())
        clock.tick(50)
    pygame.quit()

