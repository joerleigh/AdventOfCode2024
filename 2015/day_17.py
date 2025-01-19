from aoc import AdventOfCode
from functools import reduce
        
class Day17(AdventOfCode):
    """Advent of Code 2015 Day 17
    
    https://adventofcode.com/2015/day/17"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self, *args):
        eggnog = int(args[0])
        containers = [int(line) for line in self.input]
        print(len(self.ways_to_fit(eggnog, containers)))

        
    def part_two(self, *args):
        eggnog = int(args[0])
        containers = [int(line) for line in self.input]
        combos = self.ways_to_fit(eggnog, containers)
        min_containers = min([len(x) for x in combos])
        min_combos = sum([1 if len(x)==min_containers else 0 for x in combos])
        print(f'{min_combos} with {min_containers} containers')

    def ways_to_fit(self, eggnog, containers)->list[list[int]]:
        all_combos = []
        for i in range(len(containers)):
            container = containers[i]
            if eggnog == container:
                all_combos += [[container]]
            if eggnog > container:
                combos = self.ways_to_fit(eggnog-container, containers[i+1:])
                if combos is not None:
                    all_combos+= [[container, *combo] for combo in combos]
        return all_combos