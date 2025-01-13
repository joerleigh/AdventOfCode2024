#! python3
from aoc import AdventOfCode
import networkx as nx
from functools import cache

numpad_graph = nx.DiGraph()
numpad_graph.add_nodes_from(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A'])
numpad_graph.add_edges_from([
    ('7', '4'),
    ('4', '1'),
    ('8', '5'),
    ('5', '2'),
    ('2', '0'),
    ('9', '6'),
    ('6', '3'),
    ('3', 'A')
], direction='v')
numpad_graph.add_edges_from([
    ('4', '7'),
    ('1', '4'),
    ('5', '8'),
    ('2', '5'),
    ('0', '2'),
    ('6', '9'),
    ('3', '6'),
    ('A', '3')
], direction='^')
numpad_graph.add_edges_from([
    ('7', '8'),
    ('8', '9'),
    ('4', '5'),
    ('5', '6'),
    ('1', '2'),
    ('2', '3'),
    ('0', 'A')
], direction='>')
numpad_graph.add_edges_from([
    ('8', '7'),
    ('9', '8'),
    ('5', '4'),
    ('6', '5'),
    ('2', '1'),
    ('3', '2'),
    ('A', '0')
], direction='<')
arrow_graph = nx.DiGraph()

arrow_graph.add_nodes_from(['<', '>', '^', 'v', 'A'])
arrow_graph.add_edges_from([
    ('^', 'v'),
    ('A', '>')
], direction='v')
arrow_graph.add_edges_from([
    ('v', '^'),
    ('>', 'A')
], direction='^')
arrow_graph.add_edges_from([
    ('^', 'A'),
    ('<', 'v'),
    ('v', '>'),
], direction='>')
arrow_graph.add_edges_from([
    ('A', '^'),
    ('v', '<'),
    ('>', 'v'),
], direction='<')

graphs = [numpad_graph, arrow_graph, arrow_graph]

@cache
def how_to_press_numpad_button(starting_button, button_to_press, robots):
    print(f'Stepping from {starting_button} to {button_to_press}')
    paths = nx.all_shortest_paths(numpad_graph, starting_button, button_to_press)
    first_moves = [path_to_moves(numpad_graph, path) for path in paths]
    print(f'Possible moves: {first_moves}')
    shortest_move_length = float('inf')
    for move in first_moves:
        possible_shortest_move = shortest_move(move, robots)
        if possible_shortest_move<shortest_move_length:
            shortest_move_length = possible_shortest_move
    return shortest_move_length


def path_to_moves(graph, path):
    moves = [graph.get_edge_data(path[i], path[i + 1])['direction'] for i in range(len(path) - 1)]
    moves.append('A')
    moves = ''.join(moves)
    return moves

@cache
def shortest_move(buttons, robots):
    if robots == 0:
        return len(buttons)
    print(f'Calculating shortest input for {buttons} using {robots} robots')
    buttons = 'A' + buttons
    total_input_length = 0
    for i in range(1, len(buttons)):
        possible_inputs = how_to_press_arrow_button(buttons[i-1],buttons[i])
        shortest_input_length = float('inf')
        for input in possible_inputs:
            input_length = shortest_move(input, robots-1)
            if input_length<shortest_input_length:
                shortest_input_length=input_length
        total_input_length+= shortest_input_length
    return total_input_length



@cache
def how_to_press_arrow_button(starting_button, button_to_press):
    paths = nx.all_shortest_paths(arrow_graph, starting_button, button_to_press)
    all_moves = [path_to_moves(arrow_graph, path) for path in paths]
    return all_moves


class Day21(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        robots = 2
        return self.find_complexity(robots)

    def part_two(self):
        robots = 25
        return self.find_complexity(robots)

    def find_complexity(self, robots):
        total_complexity = 0
        for code in self.input:
            print(f'Inputting {code}')
            code = 'A' + code
            total_input_length = 0
            for i in range(1, len(code)):
                total_input_length += how_to_press_numpad_button(code[i - 1], code[i], robots)
            print(f'Input length: {total_input_length}')

            numerical_code = int(code[1:-1])
            complexity = total_input_length * numerical_code
            print(total_input_length, numerical_code, complexity)
            total_complexity += complexity
        return total_complexity
