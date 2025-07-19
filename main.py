import pygame
import sys
import os
from maze import generate_maze
from solver import bfs, dfs, astar
from utils import reconstruct_path, draw_grid, show_message
from main_menu import Menu

pygame.init()
pygame.mixer.init()

# Constants
CELL_SIZE = 20
FPS = 60

# Sound
CLICK_SOUND = pygame.mixer.Sound(os.path.join("assets", "click.wav"))
WIN_SOUND = pygame.mixer.Sound(os.path.join("assets", "win.wav"))

# Music
try:
    pygame.mixer.music.load(os.path.join("assets", "bg_music.mp3"))
    pygame.mixer.music.play(-1)
except Exception as e:
    print(f"[Warning] Music error: {e}")

# Game variables
level = 1
selected_algorithm = "BFS"
animate = True

# Reset Game Function
def reset_game(level):
    global maze, rows, cols, start, end, player_pos, path
    rows = cols = 10 + (level - 1) * 5
    maze = generate_maze(rows, cols)
    start = (0, 0)
    end = (rows - 1, cols - 1)
    player_pos = start
    path = []

# Main Game Function
def play_game(screen):
    global player_pos, path, level

    reset_game(level)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((255, 255, 255))
        draw_grid(screen, maze, CELL_SIZE, player_pos, path, start, end, selected_algorithm, level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game(level)
                elif event.key == pygame.K_LEFT:
                    x, y = player_pos
                    if y > 0 and maze[x][y - 1] == 0:
                        player_pos = (x, y - 1)
                elif event.key == pygame.K_RIGHT:
                    x, y = player_pos
                    if y < cols - 1 and maze[x][y + 1] == 0:
                        player_pos = (x, y + 1)
                elif event.key == pygame.K_UP:
                    x, y = player_pos
                    if x > 0 and maze[x - 1][y] == 0:
                        player_pos = (x - 1, y)
                elif event.key == pygame.K_DOWN:
                    x, y = player_pos
                    if x < rows - 1 and maze[x + 1][y] == 0:
                        player_pos = (x + 1, y)
                elif event.key == pygame.K_SPACE:
                    if selected_algorithm == "BFS":
                        path = bfs(maze, start, end, screen, CELL_SIZE, animate)
                    elif selected_algorithm == "DFS":
                        path = dfs(maze, start, end, screen, CELL_SIZE, animate)
                    elif selected_algorithm == "A*":
                        path = astar(maze, start, end, screen, CELL_SIZE, animate)
                    path = reconstruct_path(path, start, end)

        # 🎉 Check for win condition
        if player_pos == end:
            WIN_SOUND.play()
            show_message("🎉 You Win!", screen)
            pygame.time.delay(2000)
            level += 1
            reset_game(level)

        pygame.display.update()

# Setup screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Solver Game")

# Show Menu
menu = Menu(screen)
selected_algorithm = menu.run()
CLICK_SOUND.play()

# Start Game
play_game(screen)
