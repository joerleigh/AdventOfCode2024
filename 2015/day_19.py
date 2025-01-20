from functools import cache
import re

from aoc import AdventOfCode


class Day19(AdventOfCode):
    """Advent of Code 2015 Day 19
    
    https://adventofcode.com/2015/day/19"""

    def __init__(self, file):
        super().__init__(file)
        self.molecule = ""
        self.replacements = {}
        self.all_replacements = []

    def part_one(self):
        self.parse_input()

        possible_molecules = self.possible_products(self.molecule)
        print(f'There are {len(possible_molecules)} distinct molecules that can be created.')

    def possible_products(self, molecule):
        possible_molecules = []
        for i in range(len(molecule)):
            element = molecule[i:i + 1]
            if element in self.replacements:
                for product in self.replacements[element]:
                    possible_molecules.append(molecule[:i] + product + molecule[i + 1:])
            element = molecule[i:i + 2]
            if element in self.replacements:
                for product in self.replacements[element]:
                    possible_molecules.append(molecule[:i] + product + molecule[i + 2:])
        possible_molecules = set(possible_molecules)
        return possible_molecules

    def parse_input(self):
        parsing_replacements = True
        for line in self.input:
            if line == "":
                parsing_replacements = False
                continue
            if parsing_replacements:
                start, end = line.split(" => ")
                if start not in self.replacements:
                    self.replacements[start] = []
                self.replacements[start].append(end)
                self.all_replacements.append((start, end))
            else:
                self.molecule = line

    def part_two(self):
        """This part is pretty ridiculous and requires really buckling down and finding patterns in the input and
        making some inferences based off of them. This isn't a code challenge so much as a puzzle. I did not do this.
        https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/"""

        self.parse_input()
        tokens = re.findall(r'[A-Z][a-z]*', self.molecule)
        paren_tokens = re.findall(r'Rn|Ar', self.molecule)
        comma_tokens = re.findall(r'Y', self.molecule)
        print(f"{len(tokens) - len(paren_tokens) - 2 * len(comma_tokens) - 1} steps required.")
