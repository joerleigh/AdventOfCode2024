from __future__ import annotations
import re
from dataclasses import dataclass


@dataclass
class FakeComputer:
    registers: dict[str, int]
    instruction_set: list[FakeInstruction]

    pointer = 0

    def run(self, program: list[str]):
        while self.pointer<len(program):
            line = program[self.pointer]
            for instruction in self.instruction_set:
                if instruction.match_instruction(line):
                    print(f'{self.pointer}: {line} {self.registers}')
                    instruction.run(self)
                    break
            else:
                raise Exception(f"Unknown instruction: {line}")


class FakeInstruction:
    matching_regex = None
    match = None

    def match_instruction(self, line):
        match = re.match(self.matching_regex, line)
        if match:
            self.match = match
            return True
        return False

    def run(self, computer: FakeComputer):
        pass
