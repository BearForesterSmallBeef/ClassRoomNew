import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Перетаскивание")
    hold = False
    running = True
    s = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWSHOWN or event.type == pygame.WINDOWMINIMIZED:
                s += 1
                screen.fill("black")
                font = pygame.font.Font(None, 100)
                text = font.render(f"{s}", True, "red")
                text_x = width // 2 - text.get_width() // 2
                text_y = height // 2 - text.get_height() // 2
                text_w = text.get_width()
                text_h = text.get_height()
                screen.blit(text, (text_x, text_y))
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
