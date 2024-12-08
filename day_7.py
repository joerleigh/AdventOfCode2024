#! python3
from aoc import AdventOfCode


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


class Day7(AdventOfCode):
    def part_one(self):
        return self.find_solutions([add, mult])

    def part_two(self):
        return self.find_solutions([add, mult, concat])

    def find_solutions(self, operators):
        total = 0
        for line in self.input:
            value, number_str = line.split(': ')
            value = int(value)
            numbers = number_str.split()
            if self.adds_up(int(numbers[0]), numbers[1:], value, operators):
                total += value
        return total

    def adds_up(self, accumulator, numbers, value, operators):
        if len(numbers) == 0:
            return accumulator == value
        for operator in operators:
            if self.adds_up(operator(accumulator, int(numbers[0])), numbers[1:], value, operators):
                return True
        return False
