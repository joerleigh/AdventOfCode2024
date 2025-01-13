#! python3
import re

def turn_right(facing_row, facing_col):
    if facing_row == -1 and facing_col == 0:
        return 0,1
    elif facing_row == 0 and facing_col == 1:
        return 1,0
    elif facing_row == 1 and facing_col == 0:
        return 0,-1
    else: return -1,0

def set_char(string, index, char):
    return string[:index] + char + string[index + 1:]

def part_one(file):
    facing_row, facing_col = -1, 0
    col, maze, row = parse_maze(file)

    maze = solve_maze(maze, row, col, facing_row, facing_col)

    total = 0
    for line in maze:
        total += len(re.findall('X',line))
    return total

def part_two(file):
    facing_row, facing_col = -1, 0
    starting_col, maze, starting_row = parse_maze(file)

    # solve the maze once
    solved_maze = solve_maze(maze[:], starting_row, starting_col, facing_row, facing_col)

    # try putting a block in every visited space and solve again, seeing if there's a loop
    total = 0
    for row in range(len(solved_maze)):
        for col in [i for i in range(len(solved_maze[row])) if solved_maze[row].startswith('X', i)] :
            if not (row==starting_row and col==starting_col): # skip the starting position
                new_maze = maze[:]
                new_maze[row] = set_char(new_maze[row],col,'#')
                if not solve_maze(new_maze, starting_row, starting_col, facing_row, facing_col):
                    total += 1
    return total


def solve_maze(maze, row, col, facing_row, facing_col):
    max_steps = len(maze)*len(maze[0])
    step = 1
    while True:
        # mark current position
        maze[row] = set_char(maze[row], col, 'X')
        # look ahead
        next_row = row + facing_row
        next_col = col + facing_col
        if next_row < 0 or next_col < 0 or next_row >= len(maze) or next_col >= len(maze[next_row]):
            break
        if maze[next_row][next_col] == '#':
            facing_row, facing_col = turn_right(facing_row, facing_col)
        else:
            row, col = next_row, next_col
        step += 1
        if step > max_steps: #loop detected
            return False
    return maze


def parse_maze(file):
    maze = []
    row, col = -1, -1
    while line := file.readline():
        line = line.strip()
        maze.append(line)
        try:
            col = line.index('^')
            row = len(maze) - 1
        except ValueError:
            continue
    return col, maze, row