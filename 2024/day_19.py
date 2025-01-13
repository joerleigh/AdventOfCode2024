#! python3
from aoc import AdventOfCode
from functools import cache


class Day19(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.towels = self.input[0].split(', ')
        self.patterns = self.input[2:]

    def part_one(self):
        possible = 0
        for pattern in self.patterns:
            found_towels = self.first_possible_pattern(pattern)
            print(pattern, found_towels)
            if found_towels:
                possible += 1
        return possible

    def part_two(self):
        possible = 0
        for pattern in self.patterns:
            found_patterns = self.all_possible_patterns(pattern)
            print(pattern, found_patterns)
            possible += found_patterns
        return possible

    def first_possible_pattern(self, pattern):
        for towel in self.towels:
            if towel == pattern:
                return [towel]
            if towel == pattern[:len(towel)]:
                rest_of_pattern = self.first_possible_pattern(pattern[len(towel):])
                if rest_of_pattern:
                    return [towel] + rest_of_pattern
        return None

    @cache
    def all_possible_patterns(self, pattern) -> list[list[str]]:
        patterns = 0
        for towel in self.towels:
            if towel == pattern:
                patterns += 1
            elif towel == pattern[:len(towel)]:
                patterns += self.all_possible_patterns(pattern[len(towel):])
        return patterns
