#! python3
import itertools
import random

from aoc import AdventOfCode

total_bits = 45


class Day24(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.wires = {}
        self.gates = {}

    def part_one(self):
        self.parse_input()

        # while we aren't done yet, tick through the simulation. at each tick, look for gates whose input wires are
        # both defined, and store their result in their output wire. repeat until all the z wires are defined.
        loop = 0
        while not self.is_solved(self.wires):
            self.tick(self.wires, self.gates)
            loop += 1
        print(f'{loop} ticks')
        return self.solution(self.wires, 'z')

    def part_two(self):
        """This code doesn't really solve part 2. It was solved with a whole lot of faffing about, and finally solved
        manually thanks to this reddit comment
        https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3p59c6/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button"""

        self.parse_input()
        wires = self.wires.copy()
        gates = self.gates.copy()
        print(self.find_good_swap(wires, gates))

    def find_good_swap(self, wires, gates):
        problem_bit = self.find_problem_bit(wires, gates)
        print(f"Problem bit {problem_bit}")
        # outputs = sorted(list(gates.keys()))
        # outputs.remove('qjb')
        # outputs.remove('gvw')
        # outputs.remove('fbv')
        # outputs.remove('z15')
        outputs = ['z35','jbp']
        for output1, output2 in itertools.combinations(outputs, 2):
            print(output1, output2)
            tmp_wires = self.wires.copy()
            tmp_gates = gates.copy()
            self.switch_gates(output1, output2, tmp_gates)
            tmp_bit = self.find_problem_bit(tmp_wires, tmp_gates, True)
            print(f'Got to bit {tmp_bit}')
            # if tmp_bit > problem_bit:
            #     return output1, output2
        # for output1, output2 in itertools.combinations(outputs, 2):
        #     print(output1, output2)
        #     tmp_wires = self.wires.copy()
        #     tmp_gates = gates.copy()
        #     self.switch_gates(output1, output2, tmp_gates)
        #     tmp_bit = self.find_problem_bit(tmp_wires, tmp_gates, True)
        #     if tmp_bit < problem_bit:
        #         print(f"Made it worse ({tmp_bit}); pruning")
        #         continue
        #     for output3, output4 in itertools.combinations(outputs, 2):
        #         if output1 != output3 and output1 != output4 and output2 != output3 and output2 != output4:
        #             print(output1, output2, output3, output4)
        #             tmp_wires = self.wires.copy()
        #             tmp_gates = gates.copy()
        #             self.switch_gates(output1, output2, tmp_gates)
        #             self.switch_gates(output3, output4, tmp_gates)
        #             tmp_bit = self.find_problem_bit(tmp_wires, tmp_gates, True)
        #             print(f'Got to bit {tmp_bit}')
        #             if tmp_bit > problem_bit:
        #                 return output1, output2, output3, output4

    def find_problem_bit(self, wires, gates, test=False):
        for bits in range(1, 45):
            for iteration in range(bits + 10):
                if not self.run_one_test(wires, gates, bits, test):
                    return bits

    def run_one_test(self, wires, gates, n, test=False):
        self.set_n_bit(wires, n)
        x = self.solution(wires, 'x')
        y = self.solution(wires, 'y')
        loop_check = 0
        while not self.is_solved(wires):
            self.tick(wires, gates)
            loop_check += 1
            if loop_check >= 70:
                return False
        test_sum = self.solution(wires, 'z')
        if x + y != test_sum:
            return False
        return True

    def set_n_bit(self, wires, n):
        for i in wires.keys():
            wires[i] = None
        for i in range(n):
            wires[f'x{str(i).zfill(2)}'] = int(random.random() * 2)
            wires[f'y{str(i).zfill(2)}'] = int(random.random() * 2)
        for i in range(n, total_bits):
            wires[f'x{str(i).zfill(2)}'] = 0
            wires[f'y{str(i).zfill(2)}'] = 0

    def parse_input(self):
        self.wires = {}
        self.gates = {}
        getting_inputs = True
        for line in self.input:
            if line == "":
                getting_inputs = False
                continue
            if getting_inputs:
                input_node = line.split(': ')
                self.wires[input_node[0]] = int(input_node[1])
            else:
                input1, gate, input2, _, output = line.split()
                if not input1 in self.wires:
                    self.wires[input1] = None
                if not input2 in self.wires:
                    self.wires[input2] = None
                self.wires[output] = None
                self.gates[output] = (input1, gate, input2)

    def is_solved(self, wires):
        for wire in wires.keys():
            if wire.startswith('z') and wires[wire] is None:
                return False
        return True

    def tick(self, wires, gates):
        for output in gates.keys():
            input1, gate, input2 = gates[output]
            if wires[input1] is not None and wires[input2] is not None:
                match gate:
                    case 'AND':
                        wires[output] = wires[input1] & wires[input2]
                    case 'OR':
                        wires[output] = wires[input1] | wires[input2]
                    case 'XOR':
                        wires[output] = wires[input1] ^ wires[input2]

    def solution(self, wires, prefix='z'):
        zs = {}
        for wire in wires.keys():
            if wire.startswith(prefix):
                zs[int(wire[1:])] = wires[wire]
        output = ['0'] * len(zs)
        for num in zs.keys():
            output[num] = str(zs[num])
        output = ''.join(reversed(output))
        return int(output, 2)

    def switch_gates(self, output1, output2, gates):
        tmp_gate = gates[output1]
        gates[output1] = gates[output2]
        gates[output2] = tmp_gate
