#! python3
from copy import deepcopy

import aoc
from aoc import AdventOfCode


class Day8(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.input_map = aoc.Map(self.input)

    def part_one(self):
        annotated_map = deepcopy(self.input_map)
        for char in self.ALPHANUMERIC:
            antennas = self.input_map.find_all(char)
            for antenna1 in antennas:
                for antenna2 in antennas:
                    if antenna1 != antenna2:
                        antinode1 = antenna1 + (antenna1 - antenna2)
                        antinode2 = antenna2 + (antenna2 - antenna1)
                        annotated_map.set_char('#', antinode1)
                        annotated_map.set_char('#', antinode2)
        return len(annotated_map.find_all('#'))

    def part_two(self):
        annotated_map = deepcopy(self.input_map)
        for char in self.ALPHANUMERIC:
            antennas = self.input_map.find_all(char)
            for antenna1 in antennas:
                for antenna2 in antennas:
                    if antenna1 != antenna2:
                        direction1 = antenna1 - antenna2
                        direction2 = antenna2 - antenna1
                        for i in range(self.input_map.rows() + self.input_map.cols()):
                            antinode1 = antenna1 + (direction1 * i)
                            antinode2 = antenna2 + (direction2 * i)
                            annotated_map.set_char('#', antinode1)
                            annotated_map.set_char('#', antinode2)
        return len(annotated_map.find_all('#'))
