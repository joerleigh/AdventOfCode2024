from aoc import AdventOfCode
        
class Day1(AdventOfCode):
    """Advent of Code 2025 Day 1
    
    https://adventofcode.com/2025/day/1"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        position = 50
        total = 0
        for line in self.input:
            direction = line[0]
            distance = int(line[1:])
            if direction == 'L':
                distance *= -1
            position += distance
            if position % 100 == 0:
                total += 1
        print(f"Password: {total}")
        
    def part_two(self):
        position = 50
        total = 0
        for line in self.input:
            direction = line[0]
            distance = int(line[1:])
            if direction == 'L':
                direction = -1
            else:
                direction = 1
            for _ in range(distance):
                position += direction
                if position % 100 == 0:
                    total += 1
        print(f"Password: {total}")
    