import curses
from curses import wrapper
import queue
import time

maze = [
    ["😾", "🕳️", "😾", "😾", "😾", "😾", "😾", "😾", "😾"],
    ["😾", " ", " ", " ", " ", " ", " ", " ", "😾"],
    ["😾", " ", "😾", "😾", " ", "😾", "😾", " ", "😾"],
    ["😾", " ", "😾", " ", " ", " ", "😾", " ", "😾"],
    ["😾", " ", "😾", " ", "😾", " ", "😾", " ", "😾"],
    ["😾", " ", "😾", " ", "😾", " ", "😾", " ", "😾"],  
    ["😾", " ", "😾", " ", "😾", " ", "😾", "😾", "😾"],
    ["😾", " ", " ", " ", " ", " ", " ", " ", "😾"],
    ["😾", "😾", "😾", "😾", "😾", "😾", "😾", "🧀", "😾"]
]
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

    return None

def maze_print(maze, stdscr, path=[]):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i*2, j*3, "🐀")
            else:
                stdscr.addstr(i*2, j*3, value)


def find_path(maze, stdscr):
    start = "🕳️"
    end = "🧀"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        stdscr.clear()
        maze_print(maze, stdscr, path)
        time.sleep(0.3)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "😾":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  #going up
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  #going down
        neighbors.append((row + 1, col))
    if col > 0:  #going left
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  #going right
        neighbors.append((row, col + 1))

    return neighbors


def main(stdscr):
  find_path(maze, stdscr)
  stdscr.getch()
  
wrapper(main)