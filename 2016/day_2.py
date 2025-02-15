from aoc import AdventOfCode, Map, Vector


class Day2(AdventOfCode):
    """Advent of Code 2016 Day 2
    
    https://adventofcode.com/2016/day/2"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        buttons = Map(['123', '456', '789'])
        position = Vector(1,1)
        for line in self.input:
            for instruction in line:
                if instruction == 'U':
                    position.row = max(0,position.row-1)
                elif instruction == 'D':
                    position.row = min(2,position.row+1)
                elif instruction == 'L':
                    position.col = max(0,position.col-1)
                elif instruction == 'R':
                    position.col = min(2,position.col+1)
            print(buttons.value(position))
        
    def part_two(self):
        buttons = Map(['..1..', '.234.', '56789','.ABC.','..D..'])
        position = Vector(2, 0)
        for line in self.input:
            for instruction in line:
                if instruction == 'U':
                    position.row = max(0, position.row - 1)
                    if buttons.value(position)=='.':
                        position.row += 1
                elif instruction == 'D':
                    position.row = min(4, position.row + 1)
                    if buttons.value(position)=='.':
                        position.row -= 1
                elif instruction == 'L':
                    position.col = max(0, position.col - 1)
                    if buttons.value(position)=='.':
                        position.col += 1
                elif instruction == 'R':
                    position.col = min(4, position.col + 1)
                    if buttons.value(position)=='.':
                        position.col -= 1
            print(buttons.value(position))
    