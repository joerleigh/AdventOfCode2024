from aoc import AdventOfCode
import re


class Day25(AdventOfCode):
    """Advent of Code 2015 Day 25
    
    https://adventofcode.com/2015/day/25"""

    def __init__(self, file):
        super().__init__(file)
        match = re.search(r'row (\d+), column (\d+)', self.input[0])
        self.row = int(match[1])
        self.column = int(match[2])

    def part_one(self):
        # This is apparently called modular exponentiation
        first_code = 20151125
        base=252533
        mod = 33554393

        exp = int((self.row + self.column - 2) * (self.row + self.column - 1) / 2) + self.column - 1
        answer = (pow(base, exp, mod)*first_code)%mod
        print(answer)

    def part_two(self):
        print("You did it!")
