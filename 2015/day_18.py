from copy import deepcopy

import aoc.Map
from aoc import AdventOfCode, Map, Vector, COLOR_GREEN


class Day18(AdventOfCode):
    """Advent of Code 2015 Day 18
    
    https://adventofcode.com/2015/day/18"""

    def __init__(self, file):
        super().__init__(file)
        self.lights = Map(self.input)

    def part_one(self, *args):
        ticks = int(args[0])
        self.lights.set_cell_color('#', COLOR_GREEN)
        print('Initial state:')
        print(self.lights)
        current_lights = self.lights
        for i in range(ticks):
            next_lights = self.tick(current_lights)
            print()
            print(f"After {i + 1} step:")
            print(next_lights)
            current_lights = next_lights
        print(f"{len(current_lights.find_all('#'))} lights on")

    @staticmethod
    def tick(current_lights, sticky_corners=False):
        next_lights = deepcopy(current_lights)
        for light in current_lights.all_points():
            neighbors = current_lights.neighbors8(light)
            on_neighbors = sum([1 if neighbor == '#' else 0 for neighbor in neighbors])
            if current_lights.value(light) == '#':
                if on_neighbors != 2 and on_neighbors != 3:
                    next_lights.set_char('.', light)
            else:
                if on_neighbors == 3:
                    next_lights.set_char('#', light)
        if sticky_corners:
            next_lights.set_char('#', Vector(0, 0))
            next_lights.set_char('#', Vector(0, next_lights.cols() - 1))
            next_lights.set_char('#', Vector(next_lights.rows() - 1, 0))
            next_lights.set_char('#', Vector(next_lights.rows() - 1, next_lights.cols() - 1))
        return next_lights

    def part_two(self, *args):
        ticks = int(args[0])
        self.lights.set_cell_color('#', COLOR_GREEN)
        print('Initial state:')
        current_lights = self.lights
        print(current_lights.rows(), current_lights.cols())
        current_lights.set_char('#', Vector(0, 0))
        current_lights.set_char('#', Vector(0, current_lights.cols() - 1))
        current_lights.set_char('#', Vector(current_lights.rows() - 1, 0))
        current_lights.set_char('#', Vector(current_lights.rows() - 1, current_lights.cols() - 1))
        print(current_lights)
        for i in range(ticks):
            next_lights = self.tick(current_lights, True)
            print()
            print(f"After {i + 1} step:")
            print(next_lights)
            current_lights = next_lights
        print(f"{len(current_lights.find_all('#'))} lights on")
