from aoc import AdventOfCode
        
class Day2(AdventOfCode):
    """Advent of Code 2025 Day 2
    
    https://adventofcode.com/2025/day/2"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        total = 0
        for check_range in self.input[0].split(','):
            low, high = check_range.split('-')
            for check_id in range(int(low), int(high)+1):
                digits = len(str(check_id))
                if digits % 2 == 1:
                    continue
                first_half = str(check_id)[:digits//2]
                second_half = str(check_id)[digits//2:]
                if first_half == second_half:
                    total += check_id
        print(total)
        pass
        
    def part_two(self):
        total = 0
        for check_range in self.input[0].split(','):
            low, high = check_range.split('-')
            for check_id in range(int(low), int(high)+1):
                id_found = False
                total_digits = len(str(check_id))
                for parts in range(2, total_digits+1):
                    if total_digits % parts > 0:
                        continue
                    first_part = str(check_id)[:total_digits//parts]
                    matches = True
                    for part_num in range(1, parts):
                        part = str(check_id)[total_digits//parts*part_num:total_digits//parts*(part_num+1)]
                        if first_part != part:
                            matches= False
                            break
                    if matches:
                        id_found = True
                        break
                if id_found:
                    total += check_id
        print(total)
    