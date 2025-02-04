from aoc import AdventOfCode
from itertools import combinations
from functools import reduce


class Day24(AdventOfCode):
    """Advent of Code 2015 Day 24
    
    https://adventofcode.com/2015/day/24"""

    def __init__(self, file):
        super().__init__(file)
        self.packages = [int(i) for i in self.input]

    def part_one(self):
        # Look at possible first-groups, and see if there is a way to divide the rest of the packages into two equal
        # groups that equal the weight of the first group.
        min_entanglement = None
        for i in range(1, len(self.packages) - 1):
            for group1 in combinations(self.packages, i):
                rest = [p for p in self.packages if p not in group1]
                # The sum of the rest should equal twice the sum of the first group. Then see if you can split them
                # up appropriately.
                if sum(group1) * 2 == sum(rest):
                    possible=False
                    for j in range(1, len(rest)):
                        for group2 in combinations(rest, j):
                            if sum(group1) == sum(group2):
                                # It actually doesn't matter *how* we divide the other two groups, as long as we *can*, so just break
                                possible = True
                                break
                        if possible:
                            break
                    if possible:
                        print(group1, rest)
                        entanglement = reduce(lambda a,b:a*b, group1)
                        if min_entanglement is None or entanglement<min_entanglement:
                            min_entanglement = entanglement
            if min_entanglement is not None:
                break
        print(min_entanglement)

    def part_two(self):
        # Look at possible first-groups, and see if there is a way to divide the rest of the packages into two equal
        # groups that equal the weight of the first group.
        min_entanglement = None
        for i in range(1, len(self.packages) - 2):
            for group1 in combinations(self.packages, i):
                rest = [p for p in self.packages if p not in group1]
                # The sum of the rest should equal twice the sum of the first group. Then see if you can split them
                # up appropriately.
                if sum(group1) * 3 == sum(rest):
                    possible = False
                    for j in range(1, len(rest)):
                        for group2 in combinations(rest, j):
                            if sum(group1) == sum(group2):
                                other_rest = [p for p in rest if p not in group2]
                                for k in range(1, len(other_rest)):
                                    for group3 in combinations(other_rest, k):
                                        if sum(group1) == sum(group3):
                                            # It actually doesn't matter *how* we divide the other two groups, as long as we *can*, so just break
                                            possible = True
                                            break
                                    if possible:
                                        break
                        if possible:
                            break
                    if possible:
                        print(group1, rest)
                        entanglement = reduce(lambda a, b: a * b, group1)
                        if min_entanglement is None or entanglement < min_entanglement:
                            min_entanglement = entanglement
            if min_entanglement is not None:
                break
        print(min_entanglement)
