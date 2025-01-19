from aoc import AdventOfCode
import re


class Day16(AdventOfCode):
    """Advent of Code 2015 Day 16
    
    https://adventofcode.com/2015/day/16"""

    def __init__(self, file):
        super().__init__(file)
        self.clues = {}

    def part_one(self):
        parsing_clues = True
        for line in self.input:
            if line == "":
                parsing_clues = False
            else:
                if parsing_clues:
                    clue, num = line.split(': ')
                    self.clues[clue] = num
                else:
                    match = re.search(r'Sue (\d+): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)', line,
                                      re.I | re.M)
                    clue1, num1 = match[2], match[3]
                    clue2, num2 = match[4], match[5]
                    clue3, num3 = match[6], match[7]
                    if self.clues[clue1] == num1 and self.clues[clue2] == num2 and self.clues[clue3] == num3:
                        print(f'Sue {match[1]} matches!')

    def part_two(self):
        parsing_clues = True
        for line in self.input:
            if line == "":
                parsing_clues = False
            else:
                if parsing_clues:
                    clue, num = line.split(': ')
                    self.clues[clue] = num
                else:
                    match = re.search(r'Sue (\d+): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)', line,
                                      re.I | re.M)
                    clue1, num1 = match[2], match[3]
                    clue2, num2 = match[4], match[5]
                    clue3, num3 = match[6], match[7]
                    if self.clue_matches(clue1, num1) \
                            and self.clue_matches(clue2, num2) \
                            and self.clue_matches(clue3, num3):
                        print(f'Sue {match[1]} matches!')

    def clue_matches(self, clue, num):
        if clue == 'cats' or clue == 'trees':
            return num > self.clues[clue]
        elif clue == 'pomeranians' or clue == 'goldfish':
            return num < self.clues[clue]
        else:
            return num == self.clues[clue]
