from aoc import AdventOfCode, Vector


class Day1(AdventOfCode):
    """Advent of Code 2016 Day 1
    
    https://adventofcode.com/2016/day/1"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        facing = Vector.north()
        position = Vector(0, 0)
        moves = self.input[0].split(', ')
        for move in moves:
            if move[0] == 'R':
                facing = Vector.turn_right(facing)
            else:
                facing = Vector.turn_left(facing)
            distance = int(move[1:])
            position += facing * distance
        print(f'{position}: {abs(position.row) + abs(position.col)} blocks')

    def part_two(self):
        facing = Vector.north()
        positions = [Vector(0, 0)]
        moves = self.input[0].split(', ')
        for move in moves:
            position = positions[len(positions) - 1]
            if move[0] == 'R':
                facing = Vector.turn_right(facing)
            else:
                facing = Vector.turn_left(facing)
            distance = int(move[1:])
            route = [position + (facing * i) for i in range(1, distance + 1)]

            for new_position in route:
                if new_position in positions:
                    print(positions)
                    print(f'{new_position}: {abs(new_position.row) + abs(new_position.col)} blocks')
                    return
            positions += route
