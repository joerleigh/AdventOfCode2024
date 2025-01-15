import re

from aoc import AdventOfCode
        
class Day10(AdventOfCode):
    """Advent of Code 2015 Day 10
    
    https://adventofcode.com/2015/day/10"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        look = self.input[0]
        print(f'Look: {look}')
        look_and_say_re = re.compile(r'(\d)\1*')
        for i in range(40):
            say = ""
            for match in look_and_say_re.finditer(look):
                say += str(len(match[0]))
                say += str(match[1])
            look=say
        print(len(look))
        
    def part_two(self):
        look = self.input[0]
        print(f'Look: {look}')
        look_and_say_re = re.compile(r'(\d)\1*')
        for i in range(50):
            say = ""
            for match in look_and_say_re.finditer(look):
                say += str(len(match[0]))
                say += str(match[1])
            look = say
        print(len(look))
    