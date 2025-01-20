from .Vector import Vector

COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_NORMAL = "\033[0m"


class Map:
    def __init__(self, input: list[str]):
        self.map_string: list[str] = input[:]
        self.colors = {}

    @classmethod
    def blank(cls, rows, cols):
        map_input = []
        for row in range(rows):
            map_input.append(''.ljust(cols, '.'))
        return cls(map_input)

    def rows(self) -> int:
        return len(self.map_string)

    def cols(self) -> int:
        return len(self.map_string[0])

    def value(self, location: Vector) -> str | None:
        if not self.out_of_bounds(location):
            return self.map_string[location.row][location.col]
        return None

    def out_of_bounds(self, point: Vector) -> bool:
        return point.row < 0 or point.col < 0 or point.row >= len(self.map_string) \
            or point.col >= len(self.map_string[point.row])

    def set_char(self, char, point: Vector) -> None:
        if not self.out_of_bounds(point):
            self.map_string[point.row] = self.map_string[point.row][:point.col] \
                                         + char + self.map_string[point.row][point.col + 1:]

    def find_all(self, char: str) -> list[Vector]:
        all_occurrences: list[Vector] = []
        for row in range(len(self.map_string)):
            all_occurrences += [Vector(row, i) for i in range(len(self.map_string[row])) if
                                self.map_string[row].startswith(char, i)]
        return all_occurrences

    def find_first(self, char: str) -> Vector:
        for row in range(len(self.map_string)):
            all_occurrences = [Vector(row, i) for i in range(len(self.map_string[row])) if
                               self.map_string[row].startswith(char, i)]
            if len(all_occurrences) > 0:
                return all_occurrences[0]

    def all_coords(self):
        for x in range(self.cols()):
            for y in range(self.rows()):
                yield x, y

    def all_points(self):
        for x in range(self.cols()):
            for y in range(self.rows()):
                yield Vector(y, x)

    def neighbors8(self, point: Vector):
        movements = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        return [self.value(Vector(*movement) + point) for movement in movements]

    def set_cell_color(self, v, color):
        self.colors[v] = color

    def get_cell_color(self, v):
        if v in self.colors:
            return self.colors[v]
        return COLOR_NORMAL

    def print(self):
        for row in self.map_string:
            print(row)

    def __str__(self):
        """Display these values as a 2-D grid.
        Inspired by norvig’s sudoku: http://norvig.com/sudoku.html
        """
        width = 1 + max([len(str(self.map_string[y][x])) for (x, y) in self.all_coords()])
        text = ""
        for line in self.map_string:
            text += ''.join([self.get_cell_color(c) + str(c).center(width) for c in line]) + "\n"
        return text + COLOR_NORMAL
