import pygame

def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current != start:
        key = (current.row, current.col)
        if key not in parent:
            return []  # No path
        path.append(current)
        current = parent[key]
    path.append(start)
    path.reverse()
    return path

def show_message(text, screen):
    font = pygame.font.SysFont(None, 60)
    msg = font.render(text, True, (0, 128, 0))
    rect = msg.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(msg, rect)
    pygame.display.flip()

def draw_grid(screen, maze, cell_size, player_pos, path, start, end, algo_name, level):
    screen.fill((255, 255, 255))
    rows, cols = len(maze), len(maze[0])
    for row in range(rows):
        for col in range(cols):
            color = (255, 255, 255) if maze[row][col] == 0 else (0, 0, 0)
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    for node in path:
        pygame.draw.rect(screen, (0, 255, 0), (node.col * cell_size, node.row * cell_size, cell_size, cell_size))

    pygame.draw.rect(screen, (255, 0, 0), (player_pos[1] * cell_size, player_pos[0] * cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, (0, 255, 0), (end[1] * cell_size, end[0] * cell_size, cell_size, cell_size), 3)

    font = pygame.font.SysFont(None, 30)
    info = font.render(f"Alg: {algo_name} | Level: {level}", True, (100, 100, 100))
    screen.blit(info, (10, 10))
