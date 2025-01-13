#! python3
from aoc import AdventOfCode


class Day17(AdventOfCode):
    """https://adventofcode.com/2024/day/17"""

    def __init__(self, file):
        super().__init__(file)
        self.A = int(self.input[0].split(': ')[1])
        self.B = int(self.input[1].split(': ')[1])
        self.C = int(self.input[2].split(': ')[1])
        self.program = [int(i) for i in self.input[4].split(': ')[1].split(',')]
        self.pointer = 0
        self.output = []

    def part_one(self):
        while self.pointer < len(self.program):
            self.execute_instruction()
        return ','.join([str(i) for i in self.output])

    def part_two(self):
        # The key is that each loop shortens A by three digits (binary), but also depends on some unknown 3-digit
        # sequence to the left also. Working backwards through the program, try each three-digit combination and see
        # if it will yield the desired output. If yes, recurse and see if you can find a successful value for the
        # next three digits. Depth-first search, so the first value you find is the lowest possible value. This is a
        # little weird because this method will only work for the given input. deal with it.
        A = self.find_lowest_input(len(self.program) - 1, 0)

        # Just for fun, set A and run part 1:
        self.A = A
        print('Success! Checking program output: ', self.part_one())
        return A

    def find_lowest_input(self, digit, A_so_far):
        if digit < 0:
            return A_so_far
        for A_suffix in range(8):
            A = (A_so_far << 3) + A_suffix
            B = A_suffix  # 2, 4
            B = B ^ 5  # 1, 5
            C = int(A / (2 ** B))  # 7, 5
            B = B ^ C  # 4, 3
            B = B ^ 6  # 1, 6
            if B % 8 == self.program[digit]:
                # hit! recurse
                found_A = self.find_lowest_input(digit - 1, A)
                if found_A is not None:
                    return found_A
        return None

    def execute_instruction(self):
        opcode = self.program[self.pointer]
        fn = getattr(self, f'opcode_{opcode}')
        fn()

    def opcode_0(self):
        """The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The
        denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would
        divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is
        truncated to an integer and then written to the A register."""

        print(f'A = A/2**{self.combo_operand_description()}')
        numerator = self.A
        denominator = 2 ** self.combo_operand()
        self.A = int(numerator / denominator)

        self.pointer += 2

    def opcode_1(self):
        """The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal
        operand, then stores the result in register B."""

        print(f'B = B^{self.operand()}')
        self.B = self.B ^ self.operand()

        self.pointer += 2

    def opcode_2(self):
        """The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only
        its lowest 3 bits), then writes that value to the B register."""

        print(f'B = {self.combo_operand_description()}%8')
        self.B = self.combo_operand() % 8

        self.pointer += 2

    def opcode_3(self):
        """The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not
        zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction
        jumps, the instruction pointer is not increased by 2 after this instruction."""

        if self.A != 0:
            print(f'pointer = {self.operand()}')
            self.pointer = self.operand()
        else:
            self.pointer += 2

    def opcode_4(self):
        """The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the
        result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)"""

        print(f'B = B^C')
        self.B = self.B ^ self.C

        self.pointer += 2

    def opcode_5(self):
        """The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that
        value. (If a program outputs multiple values, they are separated by commas.)"""

        print(f'output {self.combo_operand_description()} % 8')
        self.output.append(self.combo_operand() % 8)

        self.pointer += 2

    def opcode_6(self):
        """The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in
        the B register. (The numerator is still read from the A register.)"""

        print(f'B = A/2**{self.combo_operand_description()}')
        numerator = self.A
        denominator = 2 ** self.combo_operand()
        self.B = int(numerator / denominator)

        self.pointer += 2

    def opcode_7(self):
        """The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in
        the C register. (The numerator is still read from the A register.)"""

        print(f'C = A/2**{self.combo_operand_description()}')
        numerator = self.A
        denominator = 2 ** self.combo_operand()
        self.C = int(numerator / denominator)

        self.pointer += 2

    def combo_operand(self):
        match self.operand():
            case 0 | 1 | 2 | 3:
                return self.operand()
            case 4:
                return self.A
            case 5:
                return self.B
            case 6:
                return self.C

    def combo_operand_description(self):
        match self.operand():
            case 0 | 1 | 2 | 3:
                return str(self.operand())
            case 4:
                return 'A'
            case 5:
                return 'B'
            case 6:
                return 'C'

    def operand(self):
        return self.program[self.pointer + 1]

    def print_status(self):
        print(f' A: {bin(self.A)}')
        print(f' B: {bin(self.B)}')
        print(f' C: {bin(self.C)}')
