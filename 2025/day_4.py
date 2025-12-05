from aoc import AdventOfCode, Map


def move_paper(map: Map) -> int:
    movable = 0
    for roll in map.find_all("@"):
        total_neighbors = 0
        for neighbor in map.neighbors8(roll):
            if neighbor == "@":
                total_neighbors += 1
        if total_neighbors < 4:
            movable += 1
            map.set_char("x", roll)
    return movable


class Day4(AdventOfCode):
    """Advent of Code 2025 Day 4
    
    https://adventofcode.com/2025/day/4"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        map = Map(self.input)
        movable = move_paper(map)
        print(movable)

    def part_two(self):
        map = Map(self.input)
        movable = -1
        total = 0
        while movable != 0:
            movable = move_paper(map)
            total += movable
        print(total)
    