from aoc import AdventOfCode
from aoc.BunchOfGates import BunchOfGates
import pprint


class Day7(AdventOfCode):
    """Advent of Code 2015 Day 7
    
    https://adventofcode.com/2015/day/7"""
    
    def __init__(self, file):
        super().__init__(file)
        self.bunch = BunchOfGates(self.input)
    
    def part_one(self):
        self.bunch.solve()
        pprint.pp(self.bunch.wires)
        
    def part_two(self):
        self.bunch.solve()
        a = self.bunch.wires['a']
        self.bunch.parse_input(self.input)
        self.bunch.gates['b'] = (self.bunch.eq_gate, a, None)
        self.bunch.solve()
        pprint.pp(self.bunch.wires)
    