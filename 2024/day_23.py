#! python3
from aoc import AdventOfCode
import networkx as nx
from itertools import combinations

class Day23(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        g = self.generate_lan_graph()

        t_triangles = []
        for clique in nx.find_cliques(g):
            if len(clique) == 3:
                if clique[0].startswith('t') or clique[1].startswith('t') or clique[2].startswith('t'):
                    t_triangles.append(tuple(sorted(clique)))
            elif len(clique) > 3:
                for triangle in combinations(clique, 3):
                    if triangle[0].startswith('t') or triangle[1].startswith('t') or triangle[2].startswith('t'):
                        t_triangles.append(tuple(sorted(triangle)))
        return len(set(t_triangles))

    def part_two(self):
        g = self.generate_lan_graph()

        max_clique = max(nx.find_cliques(g), key=len)
        return ','.join(sorted(max_clique))

    def generate_lan_graph(self):
        g = nx.Graph()
        for line in self.input:
            pair = line.split('-')
            g.add_nodes_from(pair)
            g.add_edge(pair[0], pair[1])
        return g