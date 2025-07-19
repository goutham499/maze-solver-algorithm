import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)

pygame.init()
FONT = pygame.font.SysFont(None, 40)

class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback

    def draw(self, win):
        pygame.draw.rect(win, LIGHT_GRAY, self.rect)
        pygame.draw.rect(win, BLACK, self.rect, 2)
        text = FONT.render(self.text, True, BLACK)
        win.blit(text, (self.rect.x + 10, self.rect.y + 10))

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

class Menu:
    def __init__(self, win):
        self.win = win
        self.running = True
        self.algorithm = "BFS"
        self.start_game = False
        self.quit_game = False

        self.buttons = [
            Button(200, 150, 200, 50, "Start Game", self.start),
            Button(200, 220, 200, 50, "Choose Algorithm", self.choose_algorithm),
            Button(200, 290, 200, 50, "Quit", self.quit)
        ]

    def start(self):
        self.start_game = True
        self.running = False

    def choose_algorithm(self):
        if self.algorithm == "BFS":
            self.algorithm = "DFS"
        elif self.algorithm == "DFS":
            self.algorithm = "A*"
        else:
            self.algorithm = "BFS"
        self.buttons[1].text = f"Algorithm: {self.algorithm}"

    def quit(self):
        self.quit_game = True
        self.running = False

    def run(self):
        while self.running:
            self.win.fill(WHITE)
            title = FONT.render("Maze Solver Game", True, BLACK)
            self.win.blit(title, (180, 50))

            for button in self.buttons:
                button.draw(self.win)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.click(event.pos)

        return self.start_game, self.algorithm, self.quit_game
