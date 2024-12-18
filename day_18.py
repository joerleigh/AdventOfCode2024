#! python3
from aoc import AdventOfCode, Vector, Map
import networkx as nx


class Day18(AdventOfCode):
    """https://adventofcode.com/2024/day/18"""

    def __init__(self, file):
        super().__init__(file)
        self.width, self.height, self.num = [int(a) for a in self.input[0].split(',')]
        self.falling_bytes = [Vector(int(a[1]), int(a[0])) for a in [b.split(',') for b in self.input[1:]]]

    def part_one(self):
        map = Map.blank(self.height, self.width)
        for i in range(self.num):
            map.set_char('#', self.falling_bytes[i])
        map.print()

        path = self.solve_map(map)
        return len(self.solve_map(map))-1

    def part_two(self):
        # could have done this smarter by creating a fully connected graph and removing edges as the bytes fall, rather than creating the full graph each time
        map = Map.blank(self.height, self.width)
        for i in range(len(self.falling_bytes)):
            print(f'Byte {i}')
            map.set_char('#', self.falling_bytes[i])
            try:
                self.solve_map(map)
            except nx.exception.NetworkXNoPath:
                return self.falling_bytes[i]


    def solve_map(self, map):
        empties = map.find_all('.')
        g = nx.Graph()
        g.add_nodes_from(empties)
        for location in empties:
            g.add_node(location)
            for direction in Vector.cardinal_directions():
                if map.value(location + direction) == '.':
                    g.add_edge(location, location + direction)
        return nx.shortest_path(g, Vector(0, 0), Vector(self.height - 1, self.width - 1))
