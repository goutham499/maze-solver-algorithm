import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Cell:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.x = col * size
        self.y = row * size
        self.size = size
        self.color = WHITE
        self.is_wall = True

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.size, self.size), 1)

    def set_color(self, color):
        self.color = color

class Maze:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[Cell(r, c, cell_size) for c in range(cols)] for r in range(rows)]
        self.generate_perfect_maze()

    def generate_perfect_maze(self):
        stack = []
        visited = set()
        start = self.grid[0][0]
        start.is_wall = False
        stack.append(start)
        visited.add((start.row, start.col))

        while stack:
            current = stack[-1]
            neighbors = self.get_unvisited_neighbors(current, visited)
            if neighbors:
                next_cell = random.choice(neighbors)
                self.remove_wall_between(current, next_cell)
                next_cell.is_wall = False
                stack.append(next_cell)
                visited.add((next_cell.row, next_cell.col))
            else:
                stack.pop()

        self.grid[0][0].is_wall = False
        self.grid[self.rows - 1][self.cols - 1].is_wall = False

    def get_unvisited_neighbors(self, cell, visited):
        directions = [(-2,0), (2,0), (0,-2), (0,2)]
        neighbors = []
        for dr, dc in directions:
            r, c = cell.row + dr, cell.col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols and (r, c) not in visited:
                neighbors.append(self.grid[r][c])
        return neighbors

    def remove_wall_between(self, a, b):
        r = (a.row + b.row) // 2
        c = (a.col + b.col) // 2
        self.grid[r][c].is_wall = False

    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.color = WHITE if not cell.is_wall else BLACK
                cell.draw(win)

def generate_maze(rows, cols):
    maze = Maze(rows, cols, 20)  # 20 is default cell size
    return [[1 if cell.is_wall else 0 for cell in row] for row in maze.grid]
