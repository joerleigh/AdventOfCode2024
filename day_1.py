#! python3
from aoc import AdventOfCode


class Day1(AdventOfCode):
    def part_one(self):
        first_list, second_list = self.read_lists()

        first_list.sort()
        second_list.sort()

        total = 0
        for i in range(len(first_list)):
            total += abs(first_list[i]-second_list[i])

        return total

    def part_two(self):
        first_list, second_list = self.read_lists()

        total = 0
        for first in first_list:
            found = 0
            for second in second_list:
                if first == second:
                    found+=1
            total += first * found
        return total

    def read_lists(self):
        first_list = []
        second_list = []
        for line in self.input:
            numbers = line.split()
            first_list.append(int(numbers[0]))
            second_list.append(int(numbers[1]))
        return first_list, second_list

