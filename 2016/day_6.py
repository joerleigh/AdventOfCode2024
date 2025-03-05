from aoc import AdventOfCode
from pprint import pprint
        
class Day6(AdventOfCode):
    """Advent of Code 2016 Day 6
    
    https://adventofcode.com/2016/day/6"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        num_chars = len(self.input[0])
        char_freq = [dict() for i in range(num_chars)]
        for line in self.input:
            for i in range(len(line)):
                char = line[i]
                if char not in char_freq[i].keys():
                    char_freq[i][char] = 1
                else:
                    char_freq[i][char] += 1
        pprint(char_freq)
        pprint(char_freq[0].items())
        besties = [max(i.items(), key=lambda a:a[1])[0] for i in char_freq]
        pprint(''.join(besties))
        pass
        
    def part_two(self):
        num_chars = len(self.input[0])
        char_freq = [dict() for i in range(num_chars)]
        for line in self.input:
            for i in range(len(line)):
                char = line[i]
                if char not in char_freq[i].keys():
                    char_freq[i][char] = 1
                else:
                    char_freq[i][char] += 1
        pprint(char_freq)
        pprint(char_freq[0].items())
        besties = [min(i.items(), key=lambda a: a[1])[0] for i in char_freq]
        pprint(''.join(besties))
        pass
    