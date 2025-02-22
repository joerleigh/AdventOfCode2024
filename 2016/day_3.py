from aoc import AdventOfCode
        
class Day3(AdventOfCode):
    """Advent of Code 2016 Day 3
    
    https://adventofcode.com/2016/day/3"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        possible = 0
        for line in self.input:
            sides = [int(x) for x in line.split()]
            sides.sort()
            if sides[0]+sides[1]>sides[2]:
                possible += 1
        print(f'{possible} possible triangles')
        
    def part_two(self):
        possible = 0
        tri1 = [None, None, None]
        tri2 = [None, None, None]
        tri3 = [None, None, None]
        for i in range(len(self.input)):
            line = self.input[i]
            side_num = i%3
            sides = [int(x) for x in line.split()]
            tri1[side_num] = sides[0]
            tri2[side_num] = sides[1]
            tri3[side_num] = sides[2]
            if side_num == 2:
                tri1.sort()
                if tri1[0]+tri1[1]>tri1[2]:
                    possible+=1
                tri2.sort()
                if tri2[0] + tri2[1] > tri2[2]:
                    possible += 1
                tri3.sort()
                if tri3[0] + tri3[1] > tri3[2]:
                    possible += 1
        print(f'{possible} possible triangles')