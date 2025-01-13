#! python3

def part_one(file):
    grid = []
    while line := file.readline():
        grid.append(line.strip())

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check all eight directions for a match
            total += word_matches(grid, "XMAS", row, col)
    return total


def part_two(file):
    grid = []
    while line := file.readline():
        grid.append(line.strip())

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check all eight directions for a match
            total += x_matches(grid, row, col)
    return total


def x_matches(grid, row, col):
    total = 0
    total += 1 if check_word(grid, "MAS", row - 1, col - 1, 1, 1) and check_word(grid, "MAS", row - 1, col + 1, 1,
                                                                                 -1) else 0
    total += 1 if check_word(grid, "MAS", row - 1, col - 1, 1, 1) and check_word(grid, "MAS", row + 1, col - 1, -1,
                                                                                 +1) else 0
    total += 1 if check_word(grid, "MAS", row + 1, col + 1, -1, -1) and check_word(grid, "MAS", row - 1, col + 1, 1,
                                                                                   -1) else 0
    total += 1 if check_word(grid, "MAS", row + 1, col + 1, -1, -1) and check_word(grid, "MAS", row + 1, col - 1, -1,
                                                                                   1) else 0
    return total

def word_matches(grid, word, row, col):
    total = 0
    total += 1 if check_word(grid, word, row, col, -1, -1) else 0
    total += 1 if check_word(grid, word, row, col, -1, 0) else 0
    total += 1 if check_word(grid, word, row, col, -1, 1) else 0
    total += 1 if check_word(grid, word, row, col, 0, -1) else 0
    total += 1 if check_word(grid, word, row, col, 0, 1) else 0
    total += 1 if check_word(grid, word, row, col, 1, -1) else 0
    total += 1 if check_word(grid, word, row, col, 1, 0) else 0
    total += 1 if check_word(grid, word, row, col, 1, 1) else 0
    return total


def check_word(grid, word, row, col, row_change, col_change):
    for letter in word:
        if not check_letter(grid, letter, row, col):
            return False
        row += row_change
        col += col_change
    return True


def check_letter(grid, letter, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
        return False
    return grid[row][col] == letter
