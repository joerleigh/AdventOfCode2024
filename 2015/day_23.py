from aoc import AdventOfCode
from aoc.FakeComputer import FakeInstruction, FakeComputer


class Day23(AdventOfCode):
    """Advent of Code 2015 Day 23
    
    https://adventofcode.com/2015/day/23"""

    class HalfInstruction(FakeInstruction):
        matching_regex = r'hlf ([a-z])'

        def run(self, computer: FakeComputer):
            register = self.match[1]
            computer.registers[register] = int(computer.registers[register] / 2)
            computer.pointer += 1

    class TripleInstruction(FakeInstruction):
        matching_regex = r'tpl ([a-z])'

        def run(self, computer: FakeComputer):
            register = self.match[1]
            computer.registers[register] *= 3
            computer.pointer += 1

    class IncrementInstruction(FakeInstruction):
        matching_regex = r'inc ([a-z])'

        def run(self, computer: FakeComputer):
            register = self.match[1]
            computer.registers[register] += 1
            computer.pointer += 1

    class JumpInstruction(FakeInstruction):
        matching_regex = r'jmp ([-+]\d+)'

        def run(self, computer: FakeComputer):
            offset = int(self.match[1])
            computer.pointer += offset

    class JumpIfEvenInstruction(FakeInstruction):
        matching_regex = r'jie ([a-z]), ([-+]\d+)'

        def run(self, computer: FakeComputer):
            register = self.match[1]
            offset = int(self.match[2])
            if computer.registers[register] % 2 == 0:
                computer.pointer += offset
            else:
                computer.pointer += 1

    class JumpIfOneInstruction(FakeInstruction):
        matching_regex = r'jio ([a-z]), ([-+]\d+)'

        def run(self, computer: FakeComputer):
            register = self.match[1]
            offset = int(self.match[2])
            if computer.registers[register] == 1:
                computer.pointer += offset
            else:
                computer.pointer += 1

    instruction_set = [
        HalfInstruction(),
        TripleInstruction(),
        IncrementInstruction(),
        JumpInstruction(),
        JumpIfEvenInstruction(),
        JumpIfOneInstruction(),
    ]

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        computer = FakeComputer({'a':0,'b':0},self.instruction_set)
        computer.run(self.input)
        print(computer.registers)

    def part_two(self):
        computer = FakeComputer({'a': 1, 'b': 0}, self.instruction_set)
        computer.run(self.input)
        print(computer.registers)
