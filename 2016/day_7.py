from pprint import pprint

from aoc import AdventOfCode
import re

class Day7(AdventOfCode):
    """Advent of Code 2016 Day 7
    
    https://adventofcode.com/2016/day/7"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        count = 0
        line_count = 0
        for line in self.input:
            line_count += 1
            lineIsGood = False
            matches = re.findall(r'((\w)(\w)\3\2)', line)
            if len(matches) > 0:
                if re.search(r'\[[^]]*(\w)(\w)\2\1[^\[]*]', line):
                    continue
                for match in matches:
                    if not re.search(r'(\w)\1\1\1', match[0]):
                        lineIsGood = True
                        break
            if lineIsGood:
                count += 1
        print(count)

    def part_two(self):
        count = 0
        line_count = 0
        for line in self.input:
            line_count += 1
            lineIsGood = False
            matches = re.findall(r'(?=((\w)(\w)\2[^]]*(\[|$)))', line) # the (?=(...)) is a lookahead, which lets us find overlapping matches
            if len(matches) > 0:
                for match in matches:
                    if match[1] == match[2]:
                        continue
                    if re.search(r'\[[^]]*'+match[2]+match[1]+match[2]+'[^\[]*]', line):
                        lineIsGood = True
                        break
            if lineIsGood:
                count += 1
        print(count)
    