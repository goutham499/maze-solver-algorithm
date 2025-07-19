import pygame
import heapq
from collections import deque

class Node:
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent

    def __lt__(self, other):
        return False  # needed for heapq in A*

def bfs(maze, start, end, screen=None, cell_size=20, animate=False):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    parent = {}
    queue = deque()
    queue.append(Node(start[0], start[1]))
    visited[start[0]][start[1]] = True

    while queue:
        current = queue.popleft()

        if (current.row, current.col) == end:
            return parent

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            r, c = current.row + dr, current.col + dc
            if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and maze[r][c] == 0:
                visited[r][c] = True
                next_node = Node(r, c)
                parent[(r, c)] = current
                queue.append(next_node)

                if animate and screen:
                    pygame.draw.rect(screen, (173, 216, 230), (c * cell_size, r * cell_size, cell_size, cell_size))
                    pygame.display.update()
    return {}

def dfs(maze, start, end, screen=None, cell_size=20, animate=False):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    parent = {}
    stack = [Node(start[0], start[1])]
    visited[start[0]][start[1]] = True

    while stack:
        current = stack.pop()

        if (current.row, current.col) == end:
            return parent

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            r, c = current.row + dr, current.col + dc
            if 0 <= r < rows and 0 <= c < cols and not visited[r][c] and maze[r][c] == 0:
                visited[r][c] = True
                next_node = Node(r, c)
                parent[(r, c)] = current
                stack.append(next_node)

                if animate and screen:
                    pygame.draw.rect(screen, (221, 160, 221), (c * cell_size, r * cell_size, cell_size, cell_size))
                    pygame.display.update()
    return {}

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end, screen=None, cell_size=20, animate=False):
    rows, cols = len(maze), len(maze[0])
    parent = {}
    open_set = []
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    heapq.heappush(open_set, (f_score[start], Node(start[0], start[1])))

    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        curr_pos = (current.row, current.col)

        if curr_pos == end:
            return parent

        visited.add(curr_pos)

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            r, c = current.row + dr, current.col + dc
            neighbor = (r, c)

            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0:
                temp_g = g_score[curr_pos] + 1
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f_score[neighbor] = temp_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], Node(r, c)))
                    parent[neighbor] = current

                    if animate and screen and neighbor not in visited:
                        pygame.draw.rect(screen, (144, 238, 144), (c * cell_size, r * cell_size, cell_size, cell_size))
                        pygame.display.update()

    return {}
