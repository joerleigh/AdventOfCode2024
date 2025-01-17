from fontTools.ttLib.tables.S_V_G_ import doc_index_entry_format_0

from aoc import AdventOfCode
import re


class Day14(AdventOfCode):
    """Advent of Code 2015 Day 14
    
    https://adventofcode.com/2015/day/14"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self, *args):
        if len(args) < 1:
            print("No duration provided")
            return
        duration = int(args[0])
        for line in self.input:
            match = re.search(r'^([a-z]+)[^\d]+(\d+)[^\d]+(\d+)[^\d]+(\d+)', line, re.I | re.M)
            name = match[1]
            speed = int(match[2])
            sprint = int(match[3])
            rest = int(match[4])
            full_cycles = int(duration / (sprint + rest))
            remainder = duration % (sprint + rest)
            if remainder > sprint:
                full_cycles += 1
                remainder = 0
            distance = full_cycles * sprint * speed + remainder * speed
            print(name, distance)

    def part_two(self, *args):
        if len(args) < 1:
            print("No duration provided")
            return
        duration = int(args[0])
        reindeers = []
        for line in self.input:
            match = re.search(r'^([a-z]+)[^\d]+(\d+)[^\d]+(\d+)[^\d]+(\d+)', line, re.I | re.M)
            name = match[1]
            speed = int(match[2])
            sprint = int(match[3])
            rest = int(match[4])
            reindeer = Reindeer(name, speed, sprint, rest)
            reindeer.plot_distance(duration)
            reindeers.append(reindeer)
        for time in range(duration):
            furthest_distance = 0
            furthest_reindeer = None
            for reindeer in reindeers:
                if reindeer.distance[time]>furthest_distance:
                    furthest_distance = reindeer.distance[time]
                    furthest_reindeer = reindeer
            furthest_reindeer.points+=1
        for reindeer in reindeers:
            print(reindeer.name, reindeer.points)



class Reindeer:
    def __init__(self, name, speed, sprint, rest):
        self.name = name
        self.speed = speed
        self.sprint = sprint
        self.rest = rest

        self.distance = []
        self.points = 0

    def plot_distance(self, duration):
        time = 0
        sprinting = True
        last_position = 0
        while time < duration:
            if time > 0:
                last_position = self.distance[time - 1]
            if sprinting:
                self.distance += [last_position + (i+1) * self.speed for i in range(self.sprint)]
                time += self.sprint
            else:
                self.distance += [last_position for i in range(self.rest)]
                time += self.rest
            sprinting = not sprinting
