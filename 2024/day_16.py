#! python3
from aoc import AdventOfCode, Map, Vector
import networkx as nx


class Day16(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.map = Map(self.input)

    def part_one(self) -> int:
        g, start, end = self.build_graph()

        # find shortest path
        path = nx.shortest_path(g, (start, Vector.east()), end, weight='cost')
        print('Shortest path: ', path)

        return nx.path_weight(g, path, 'cost')

    def part_two(self) -> int:
        g, start, end = self.build_graph()
        all_tiles = []
        for path in nx.all_shortest_paths(g, (start, Vector.east()), end, weight='cost'):
            all_tiles += [node[0] if type(node)==tuple else node for node in path]
        distinct_tiles = set(all_tiles)
        return len(distinct_tiles)

    def build_graph(self):
        start = self.map.find_all('S')[0]
        end = self.map.find_all('E')[0]
        empties = self.map.find_all('.')
        empties.append(start)
        g = nx.DiGraph()
        g.add_node(end)
        for direction in Vector.cardinal_directions():
            g.add_nodes_from([(e, direction) for e in empties])
        for location in empties:
            for direction in Vector.cardinal_directions():
                # add edges for rotating in place
                next_direction = Vector.turn_right(direction)
                g.add_edge((location, direction), (location, next_direction), cost=1000)
                g.add_edge((location, next_direction), (location, direction), cost=1000)

                # add edges for moving in a straight line, when there's not a wall
                neighbor = location + direction
                if self.map.value(neighbor) == '.':
                    g.add_edge((location, direction), (neighbor, direction), cost=1)
                elif self.map.value(neighbor) == 'E':
                    g.add_edge((location, direction), end, cost=1)
        return g, start, end
