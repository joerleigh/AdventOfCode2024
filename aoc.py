#! python3

import os
from typing import Literal, List


class Vector:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col

    @staticmethod
    def north():
        return Vector(-1, 0)

    @staticmethod
    def east():
        return Vector(0, 1)

    @staticmethod
    def south():
        return Vector(1, 0)

    @staticmethod
    def west():
        return Vector(0, -1)

    @staticmethod
    def turn_right(facing):
        if facing == Vector.north():
            return Vector.east()
        elif facing == Vector.east():
            return Vector.south()
        elif facing == Vector.south():
            return Vector.west()
        else:
            return Vector.north()

    def __add__(self, other):
        return Vector(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Vector(self.row - other.row, self.col - other.col)

    def __mul__(self, other):
        return Vector(self.row * other, self.col * other)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __str__(self):
        return f'[{self.row},{self.col}]'
    def __repr__(self):
        return self.__str__()
    def __hash__(self):
        return hash((self.row,self.col))


class Map:
    def __init__(self, input):
        self.map_string: List[str] = input

    def rows(self):
        return len(self.map_string)

    def cols(self):
        return len(self.map_string[0])

    def value(self, location: Vector):
        if not self.out_of_bounds(location):
            return self.map_string[location.row][location.col]
        return None

    def out_of_bounds(self, point: Vector):
        return point.row < 0 or point.col < 0 or point.row >= len(self.map_string) \
            or point.col >= len(self.map_string[point.row])

    def set_char(self, char, point: Vector):
        if not self.out_of_bounds(point):
            self.map_string[point.row] = self.map_string[point.row][:point.col] \
                                         + char + self.map_string[point.row][point.col + 1:]

    def find_all(self, char: str):
        all_occurrences: List[Vector] = []
        for row in range(len(self.map_string)):
            all_occurrences += [Vector(row, i) for i in range(len(self.map_string[row])) if
                                self.map_string[row].startswith(char, i)]
        return all_occurrences


class AdventOfCode:
    alphanumeric = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, file):
        self.input: List[str] = []
        self.file = file
        self.parse_file()

    def part_one(self) -> int:
        pass

    def part_two(self) -> int:
        pass

    def run(self, part: Literal[1, 2]) -> int | None:
        if part == 1:
            return self.part_one()
        elif part == 2:
            return self.part_two()
        return None

    def parse_file(self):
        self.input = []
        while line := self.file.readline():
            line = line.strip()
            self.input.append(line)


def run_day(day: int, part: Literal[1, 2], use_sample: bool) -> int:
    suffix = '_sample' if use_sample else ''
    filename = f'inputs/day_{day}_{part}{suffix}.txt'
    if not os.path.isfile(filename):
        filename = f'inputs/day_{day}{suffix}.txt'

    modulename = f'day_{day}'
    day_module = __import__(modulename)

    try:
        class_name = f'Day{day}'
        class_ = getattr(day_module, class_name)
        print(f'Loading day {day}, part {part} from {class_name} class')
        with open(filename) as file:
            day_class: AdventOfCode = class_(file)
            return day_class.run(part)

    except AttributeError:
        print(f'Loading day {day}, part {part} from {modulename} module')
        with open(filename) as file:
            if part == 1:
                return day_module.part_one(file)
            elif part == 2:
                return day_module.part_two(file)
