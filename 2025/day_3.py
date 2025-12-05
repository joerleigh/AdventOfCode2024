from aoc import AdventOfCode


def first_max_digit(line, start, end):
    max_digit = "0"
    max_digit_index = -1
    for digit_index in range(start, end):
        if(line[digit_index] > max_digit):
            max_digit = line[digit_index]
            max_digit_index = digit_index
    return (max_digit, max_digit_index)

def max_number(line, digits):
    number = ""
    start = 0
    end = len(line)-(digits-1)
    for i in range(digits):
        digit, digit_index = first_max_digit(line, start, end)
        number += digit
        start = digit_index+1
        end += 1
    return int(number)

class Day3(AdventOfCode):
    """Advent of Code 2025 Day 3
    
    https://adventofcode.com/2025/day/3"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        total = 0
        for line in self.input:
            joltage = max_number(line, 2)
            print(joltage)
            total += joltage
        print(total)
        
    def part_two(self):
        total = 0
        for line in self.input:
            joltage = max_number(line, 12)
            print(joltage)
            total += joltage
        print(total)

