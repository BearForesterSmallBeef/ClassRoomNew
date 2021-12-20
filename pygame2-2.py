import pygame


class Board:
    # создаем клетчатое поле
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * height for _ in range(width)]
        # значения по умолчанию
        self.left, self.top, self.cell_size = 10, 10, 30
        self.cords = (0, 0)
        self.cell = (None, None)

    def render(self, screen):
        for row in range(self.width):
            for col in range(self.height):
                pygame.draw.rect(screen, "white", (self.left + self.cell_size * row,
                                                   self.top + self.cell_size * col, self.cell_size,
                                                   self.cell_size), self.board[row][col])

    def set_view(self, left=10, top=10, cell_size=30):
        self.left, self.top, self.cell_size = left, top, cell_size

    def on_click(self, cords):
        self.board[cords[0]][cords[1]] = int(not(self.board[cords[0]][cords[1]]))

    def get_click(self, cords):
        self.cords = cords
        self.cell = self.get_cell(cords)
        self.on_click(self.cell)

    def get_cell(self, cords):
        x = (cords[0] - self.left) // self.cell_size
        if x < 0 or x > self.width:
            x = None
        y = (cords[1] - self.top) // self.cell_size
        if y < 0 or y > self.height:
            y = None
        return x, y


def main():
    board = Board(3, 3)
    board.set_view(100, 100, 50)
    pygame.init()
    size = width, height = 800, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Клетки")
    running = True

    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 60)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill("black")
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()