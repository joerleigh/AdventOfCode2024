import pprint
import re

from aoc import AdventOfCode


class Day8(AdventOfCode):
    """Advent of Code 2015 Day 8
    
    https://adventofcode.com/2015/day/8"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        code_length = 0
        mem_length = 0
        escape_code_re = re.compile(r'^\\x[0-9a-f]{2}', re.I)
        for line in self.input:
            line_code_length = len(line)
            line_mem_length = -2
            i = 0
            while i < len(line):
                line_mem_length += 1
                if line[i:].startswith(r'\\'):
                    i += 2
                elif line[i:].startswith(r'\"'):
                    i += 2
                elif escape_code_re.match(line[i:]):
                    i += 4
                else:
                    i += 1
            code_length += line_code_length
            mem_length += line_mem_length
            print(line, line_code_length, line_mem_length)
        print(code_length, mem_length, code_length - mem_length)

    def part_two(self):
        code_length = 0
        mem_length = 0
        for line in self.input:
            line_code_length = len(line)
            line_mem_length = line_code_length+2
            line_mem_length += len(re.findall(r'\\', line))
            line_mem_length += len(re.findall(r'"', line))
            code_length += line_code_length
            mem_length += line_mem_length
            print(line, line_code_length, line_mem_length)
        print(code_length, mem_length, mem_length - code_length)
