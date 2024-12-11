#! python3
from aoc import AdventOfCode, Map, Vector


class Day10(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.input_map = Map(self.input)

    def part_one(self) -> int:
        potential_trailheads = self.input_map.find_all('0')
        total_trails = 0
        for trailhead in potential_trailheads:
            print(f'Looking from {trailhead.row},{trailhead.col}')
            trails = set(self.look_for_trails(trailhead))
            print(f'Found {len(trails)}')
            total_trails += len(trails)
        return total_trails

    def part_two(self) -> int:
        potential_trailheads = self.input_map.find_all('0')
        total_rating = 0
        for trailhead in potential_trailheads:
            print(f'Looking from {trailhead.row},{trailhead.col}')
            trails = self.rate_trails(trailhead)
            print(f'Found {trails}')
            total_rating += trails
        return total_rating

    def look_for_trails(self, location):
        elevation = int(self.input_map.value(location))
        if elevation == 9:
            return [location]
        trails_found = []
        for direction in [Vector.north(), Vector.east(), Vector.south(), Vector.west()]:
            if not self.input_map.out_of_bounds(location + direction) \
                    and int(self.input_map.value(location + direction)) == elevation + 1:
                trails_found += self.look_for_trails(location + direction)
        return trails_found

    def rate_trails(self, location):
        elevation = int(self.input_map.value(location))
        if elevation == 9:
            return 1
        trails_found = 0
        for direction in [Vector.north(), Vector.east(), Vector.south(), Vector.west()]:
            if not self.input_map.out_of_bounds(location + direction) \
                    and int(self.input_map.value(location + direction)) == elevation + 1:
                trails_found += self.rate_trails(location + direction)
        return trails_found
