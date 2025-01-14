from aoc import AdventOfCode
import networkx as nx
import itertools


class Day9(AdventOfCode):
    """Advent of Code 2015 Day 9
    
    https://adventofcode.com/2015/day/9"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        g = nx.Graph()
        for line in self.input:
            a, _, b, _, distance = line.split()
            g.add_node(a)
            g.add_node(b)
            g.add_edge(a, b, distance=int(distance))

        shortest_distance = None
        for path in (itertools.permutations(g.nodes, len(g.nodes))):
            distance = nx.path_weight(g, path, 'distance')
            print(path, distance)
            if shortest_distance is None or distance < shortest_distance:
                shortest_distance = distance
        print(f'Shortest distance: {shortest_distance}')

    def part_two(self):
        g = nx.Graph()
        for line in self.input:
            a, _, b, _, distance = line.split()
            g.add_node(a)
            g.add_node(b)
            g.add_edge(a, b, distance=int(distance))

        longest_distance = None
        for path in (itertools.permutations(g.nodes, len(g.nodes))):
            distance = nx.path_weight(g, path, 'distance')
            print(path, distance)
            if longest_distance is None or distance > longest_distance:
                longest_distance = distance
        print(f'Shortest distance: {longest_distance}')
