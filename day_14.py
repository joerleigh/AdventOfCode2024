#! python3
from aoc import AdventOfCode, Map, Vector
from PIL import Image


class Robot:
    def __init__(self, start_row, start_col, velocity_row, velocity_col):
        self.position = Vector(start_row, start_col)
        self.velocity = Vector(velocity_row, velocity_col)


class Day14(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.width, self.height = self.input[0].split()
        self.width = int(self.width)
        self.height = int(self.height)
        self.robots = self.parse_robots(self.input[1:])

    def part_one(self) -> int:
        seconds = 100
        self.move_robots(seconds)
        self.show_robot_image()
        return self.safety_factor()

    def part_two(self) -> int:
        img_rows = 90
        img_cols = 101
        img = self.image_grid(img_rows, img_cols)
        pixels = img.load()
        found_the_tree = 0
        for i in range(img_rows * img_cols):
            row = int(i / img_cols)
            col = i % img_cols
            self.move_robots(1)
            if len(self.robot_map().find_all('#######'))>0:
                self.add_robots(pixels, row, col, (0, 255, 0))
                found_the_tree = i+1
            else:
                self.add_robots(pixels, row, col)
        img.show()
        return found_the_tree

    def move_robots(self, seconds):
        for robot in self.robots:
            robot.position = robot.position + robot.velocity * seconds
            robot.position.row %= self.height
            robot.position.col %= self.width

    @staticmethod
    def parse_robots(robot_input):
        robots = []
        for line in robot_input:
            start_str, velocity_str = line.split()
            start_col, start_row = start_str.split('=')[1].split(',')
            velocity_col, velocity_row = velocity_str.split('=')[1].split(',')
            robots.append(Robot(int(start_row), int(start_col), int(velocity_row), int(velocity_col)))
        return robots

    def safety_factor(self):
        middle_row = int((self.height - 1) / 2)
        middle_col = int((self.width - 1) / 2)
        print(f'Ignoring {middle_col, middle_row}')
        quadrants = [0, 0, 0, 0]
        for robot in self.robots:
            if robot.position.row < middle_row and robot.position.col < middle_col:
                quadrants[0] += 1
            elif robot.position.row < middle_row and robot.position.col > middle_col:
                quadrants[1] += 1
            elif robot.position.row > middle_row and robot.position.col < middle_col:
                quadrants[2] += 1
            elif robot.position.row > middle_row and robot.position.col > middle_col:
                quadrants[3] += 1
        print(quadrants)
        return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

    def print_robots(self, with_safety: bool = False):
        map = self.robot_map(with_safety)
        map.print()

    def robot_map(self, with_safety: bool = False):
        map = Map.blank(self.height, self.width)
        for robot in self.robots:
            map.set_char('#', robot.position)
        if with_safety:
            middle_row = int((self.height - 1) / 2)
            middle_col = int((self.width - 1) / 2)
            for row in range(map.rows()):
                map.set_char(' ', Vector(row, middle_col))
            for col in range(map.cols()):
                map.set_char(' ', Vector(middle_row, col))
        return map

    def show_robot_image(self):
        img = Image.new('1', (self.width, self.height), "black")
        pixels = img.load()
        self.add_robots(pixels)
        img.show()

    def image_grid(self, rows, cols):
        img = Image.new('RGB', (self.width * cols, self.height * rows))
        return img

    def add_robots(self, pixels, offset_row: int = 0, offset_col: int = 0, value=(255, 255, 255)):
        for robot in self.robots:
            pixels[robot.position.col + offset_col * self.width, robot.position.row + offset_row * self.height] = value
