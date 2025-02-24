from aoc import AdventOfCode
from hashlib import md5
import re

class Day5(AdventOfCode):
    """Advent of Code 2016 Day 5
    
    https://adventofcode.com/2016/day/5"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        digit_re = re.compile(r'^00000(\w)')
        password = ""
        door_id = self.input[0]
        salt = 0
        while len(password)<8:
            match = digit_re.match(md5(f'{door_id}{salt}'.encode()).hexdigest())
            if match:
                password += match[1]
                print(f'Found digit: {match[1]}')
            salt += 1
        print(password)
        
    def part_two(self):
        digit_re = re.compile(r'^00000([0-7])(\w)')
        password = [None]*8
        door_id = self.input[0]
        salt = 0
        while None in password:
            match = digit_re.match(md5(f'{door_id}{salt}'.encode()).hexdigest())
            if match and password[int(match[1])] is None:
                password[int(match[1])] = match[2]
                print(f'Found digit {match[1]}: {match[2]}')
            salt += 1
        print(''.join(password))

    