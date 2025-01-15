import itertools

from aoc import AdventOfCode
import re
from pprint import pp


class Day13(AdventOfCode):
    """Advent of Code 2015 Day 13
    
    https://adventofcode.com/2015/day/13"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        happiness = self.happiness_matrix()
        pp(happiness)
        max_happiness = self.get_max_happiness(happiness)
        print(max_happiness)

    def get_max_happiness(self, happiness):
        max_happiness = 0
        for combo in itertools.permutations(happiness.keys(), len(happiness)):
            print(combo)
            total_happiness = 0
            for i in range(len(combo)):
                total_happiness += happiness[combo[i]][combo[(i - 1) % len(combo)]]
                total_happiness += happiness[combo[i]][combo[(i + 1) % len(combo)]]
            print(total_happiness)
            max_happiness = max(max_happiness, total_happiness)
        return max_happiness

    def happiness_matrix(self):
        happiness = {}
        for line in self.input:
            match = re.search(r'^([a-z]+).*(gain|lose) (\d+).*?([a-z]+)\.$', line, re.I | re.M)
            a = match[1]
            b = match[4]
            sign = match[2]
            gain = int(match[3])
            if a not in happiness:
                happiness[a] = {}
            if sign == 'lose':
                gain = gain * -1
            happiness[a][b] = gain
        return happiness

    def part_two(self):
        happiness = self.happiness_matrix()
        people = happiness.keys()
        happiness['me'] = {}
        for person in people:
            happiness['me'][person] = 0
            happiness[person]['me'] = 0
        pp(happiness)
        max_happiness = self.get_max_happiness(happiness)
        print(max_happiness)
