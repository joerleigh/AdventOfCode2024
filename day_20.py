#! python
from aoc import AdventOfCode, Map, Vector


class Day20(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.map = Map(self.input)

    def part_one(self):
        start = self.map.find_first('S')
        # it's labyrinth, not a maze, so just find the first path to the end and order the spaces from start to
        # finish. Then, loop through and look for any two spaces that are exactly two spaces apart in any direction (
        # but more than two steps apart in the list). The number of steps apart minus two is the number of steps
        # saved. O(N^2) time.
        threshold = 100
        path = [start]
        self.solve_labyrinth(path)
        print(path)
        above_threshold = self.find_cheats(path, threshold, 2)
        print(f'{above_threshold} shortcuts save at least {threshold} seconds')
        return above_threshold

    def part_two(self):
        start = self.map.find_first('S')
        # it's labyrinth, not a maze, so just find the first path to the end and order the spaces from start to
        # finish. Then, loop through and look for any two spaces that are exactly two spaces apart in any direction (
        # but more than two steps apart in the list). The number of steps apart minus two is the number of steps
        # saved. O(N^2) time.
        threshold = 100
        path = [start]
        self.solve_labyrinth(path)
        print(path)
        above_threshold = self.find_cheats(path, threshold, 20)
        print(f'{above_threshold} shortcuts save at least {threshold} seconds')
        return above_threshold

    def find_cheats(self, path, threshold, max_cheat_length):
        above_threshold = 0
        for i in range(len(path) - 4):
            for j in range(i + 4, len(path)):
                cheat_length = abs(path[i].row - path[j].row) + abs(path[i].col - path[j].col)
                saved_time = j - i - cheat_length
                if cheat_length <= max_cheat_length and saved_time > 0:
                    # shortcut found!
                    print(f'Shortcut between {path[i]} and {path[j]} saves {saved_time} picoseconds')
                    if saved_time >= threshold:
                        above_threshold += 1
        return above_threshold

    def solve_labyrinth(self, path):
        while True:
            location = path[len(path) - 1]
            previous_location = path[len(path) - 2]
            for direction in Vector.cardinal_directions():
                neighbor = location + direction
                if neighbor != previous_location:
                    if self.map.value(neighbor) == '.':
                        path.append(neighbor)
                    elif self.map.value(neighbor) == 'E':
                        path.append(neighbor)
                        return
