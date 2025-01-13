#! python3
from aoc import AdventOfCode
import re


class ClawMachine:
    def __init__(self, a_x, a_y, b_x, b_y, p_x, p_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.p_x = p_x
        self.p_y = p_y

    def solve(self) -> (float, float):
        a_presses = (self.p_x * self.b_y - self.p_y * self.b_x) / (self.b_y * self.a_x - self.b_x * self.a_y)
        b_presses = (self.p_y * self.a_x - self.p_x * self.a_y) / (self.b_y * self.a_x - self.b_x * self.a_y)
        return a_presses, b_presses


class Day13(AdventOfCode):
    def part_one(self) -> int:
        re_a = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
        re_b = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
        re_p = re.compile(r'Prize: X=(\d+), Y=(\d+)')
        a_x, a_y, b_x, b_y, p_x, p_y = None, None, None, None, None, None
        cost_a = 3
        cost_b = 1
        cost = 0
        for line in self.input:
            line = line.strip()
            if line == '':
                machine = ClawMachine(a_x, a_y, b_x, b_y, p_x, p_y)
                a, b = machine.solve()
                if a.is_integer() and b.is_integer():
                    cost += cost_a*int(a)+cost_b*int(b)
                continue

            match_a = re_a.match(line)
            if match_a:
                a_x, a_y = int(match_a[1]), int(match_a[2])
                continue

            match_b = re_b.match(line)
            if match_b:
                b_x, b_y = int(match_b[1]), int(match_b[2])
                continue

            match_p = re_p.match(line)
            if match_p:
                p_x, p_y = int(match_p[1]), int(match_p[2])
                continue
        # run one more time, because we don't have a blank line after the last set
        machine = ClawMachine(a_x, a_y, b_x, b_y, p_x, p_y)
        a, b = machine.solve()
        if a.is_integer() and b.is_integer():
            cost += cost_a * int(a) + cost_b * int(b)
        return cost

    def part_two(self) -> int:
        re_a = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
        re_b = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
        re_p = re.compile(r'Prize: X=(\d+), Y=(\d+)')
        a_x, a_y, b_x, b_y, p_x, p_y = None, None, None, None, None, None
        cost_a = 3
        cost_b = 1
        cost = 0
        for line in self.input:
            line = line.strip()
            if line == '':
                machine = ClawMachine(a_x, a_y, b_x, b_y, p_x, p_y)
                a, b = machine.solve()
                if a.is_integer() and b.is_integer():
                    cost += cost_a*int(a)+cost_b*int(b)
                continue

            match_a = re_a.match(line)
            if match_a:
                a_x, a_y = int(match_a[1]), int(match_a[2])
                continue

            match_b = re_b.match(line)
            if match_b:
                b_x, b_y = int(match_b[1]), int(match_b[2])
                continue

            match_p = re_p.match(line)
            if match_p:
                p_x, p_y = int(match_p[1])+10000000000000, int(match_p[2])+10000000000000
                continue
        # run one more time, because we don't have a blank line after the last set
        machine = ClawMachine(a_x, a_y, b_x, b_y, p_x, p_y)
        a, b = machine.solve()
        if a.is_integer() and b.is_integer():
            cost += cost_a * int(a) + cost_b * int(b)
        return cost