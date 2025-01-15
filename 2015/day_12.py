from aoc import AdventOfCode
import re
import json


def json_value(data):
    data_sum = 0
    if isinstance(data, list):
        for value in data:
            data_sum += json_value(value)
    elif isinstance(data, dict):
        for key in data.keys():
            if data[key] == 'red':
                return 0
            data_sum += json_value(data[key])
    elif isinstance(data, int):
        data_sum += data
    return data_sum


class Day12(AdventOfCode):
    """Advent of Code 2015 Day 12
    
    https://adventofcode.com/2015/day/12"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        data = self.input[0]
        sum = 0
        nums = re.findall(r'-?\d+', data, re.I | re.S | re.M)
        for num in nums:
            sum += int(num)
        print(f'Sum: {sum}')

    def part_two(self):
        data = json.loads(self.input[0])
        sum = json_value(data)
        print(f'Sum: {sum}')
