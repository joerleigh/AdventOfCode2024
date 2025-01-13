#! python3
from aoc import AdventOfCode, Map, Vector


class Day12(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.input_map = Map(self.input)
        self.coverage_map = Map(self.input)

    def part_one(self) -> int:
        cost = 0
        for row in range(self.input_map.rows()):
            for col in range(self.input_map.cols()):
                location = Vector(row, col)
                if self.coverage_map.value(location) != '#':
                    area, perimeter = self.walk(location, 0, 0)
                    print(self.input_map.value(location), area, perimeter)
                    cost += area * perimeter
        return cost

    def part_two(self) -> int:
        cost = 0
        for row in range(self.input_map.rows()):
            for col in range(self.input_map.cols()):
                location = Vector(row, col)
                if self.coverage_map.value(location) != '#':
                    area, sides = self.bulk_walk(location, 0, 0)
                    print(self.input_map.value(location), area, sides)
                    cost += area * sides
        return cost

    def walk(self, location: Vector, area: int, perimeter: int):
        # if already covered, ignore and return
        if self.coverage_map.value(location) == '#':
            return area, perimeter
        # mark coverage and increase area by 1
        self.coverage_map.set_char('#', location)
        area += 1
        # check the four neighbors
        plant = self.input_map.value(location)
        for direction in [Vector.north(), Vector.east(), Vector.south(), Vector.west()]:
            neighbor = location + direction
            # if the neighbor is a different plant, increase perimeter by 1
            if self.input_map.value(neighbor) != plant:
                perimeter += 1
            # if the neighbor is the same plant, continue walk from there
            else:
                area, perimeter = self.walk(neighbor, area, perimeter)
        return area, perimeter

    def bulk_walk(self, location: Vector, area: int, sides: int):
        # if already covered, ignore and return
        if self.coverage_map.value(location) == '#':
            return area, sides
        # mark coverage and increase area by 1
        self.coverage_map.set_char('#', location)
        area += 1
        # check the four neighbors
        plant = self.input_map.value(location)
        for direction in Vector.cardinal_directions():
            neighbor = location + direction
            # find all the corners to count the sides
            # if two adjacent neighbors are not this plant, that's an outside corner.
            next_neighbor = location + Vector.turn_right(direction)
            if self.input_map.value(neighbor) != plant and self.input_map.value(next_neighbor) != plant:
                sides += 1

            # if two adjacent neighbors are this plant but the diagonal isn't, that's an inside corner
            diagonal_neighbor = location + direction + Vector.turn_right(direction)
            if self.input_map.value(neighbor) == plant \
                    and self.input_map.value(next_neighbor) == plant \
                    and self.input_map.value(diagonal_neighbor) != plant:
                sides += 1

            # if the neighbor is the same plant, continue walk from there
            if self.input_map.value(neighbor) == plant:
                area, sides = self.bulk_walk(neighbor, area, sides)
        return area, sides
