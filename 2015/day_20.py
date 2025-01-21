from functools import reduce
from math import sqrt

from aoc import AdventOfCode


class Day20(AdventOfCode):
    """Advent of Code 2015 Day 20
    
    https://adventofcode.com/2015/day/20"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        present_threshold = int(self.input[0])
        min_n = int(-0.5 + sqrt(1 / 4 + 2 * present_threshold))
        for i in range(min_n, int(present_threshold / 10)):
            presents = self.presents(i)
            if presents >= present_threshold:
                print(f'House {i} gets {presents} presents')
                return

    def part_two(self):
        present_threshold = int(self.input[0])
        min_n = int(-0.5 + sqrt(1 / 4 + 2 * present_threshold))
        for i in range(min_n, int(present_threshold / 10)):
            presents = self.presents2(i)
            if presents >= present_threshold:
                print(f'House {i} gets {presents} presents')
                return

    def presents(self, house):
        presents = 0
        for i in self.factors(house):
            presents += i * 10
        print(house, presents)
        return presents

    def presents2(self, house):
        presents = 0
        for factor in self.factors(house):
            if house/factor <= 50:
                presents += factor * 11
        print(house, presents)
        return presents

    @staticmethod
    def factors(n):
        return set(reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
