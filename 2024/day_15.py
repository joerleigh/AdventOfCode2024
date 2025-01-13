#! python3
from aoc import AdventOfCode, Map, Vector
from functools import cmp_to_key


class Day15(AdventOfCode):
    BOX = 'O'
    BOX_LEFT = '['
    BOX_RIGHT = ']'
    WALL = '#'
    EMPTY = '.'
    ROBOT = '@'

    def __init__(self, file):
        super().__init__(file)
        midpoint = None
        for i in range(len(self.input)):
            if self.input[i] == '':
                midpoint = i
                break
        self.map = Map(self.input[:midpoint])
        self.instructions = ''.join(self.input[midpoint + 1:])
        self.robot = self.map.find_all(self.ROBOT)[0]

    def part_one(self) -> int:
        for instruction in self.instructions:
            self.try_to_move(instruction)
        self.map.print()
        return self.gps_sum()

    def part_two(self) -> int:
        self.map.print()
        self.scale_up()
        for instruction in self.instructions:
            self.try_to_move(instruction)
        self.map.print()
        return self.gps_sum()

    def try_to_move(self, instruction):
        print(instruction)
        direction = self.get_direction(instruction)
        next_location = self.robot + direction
        neighbor = self.map.value(next_location)
        match neighbor:
            case self.WALL:
                # can't move into wall, do nothing
                pass
            case self.EMPTY:
                # move into empty space
                self.move_robot(direction, next_location)
            case self.BOX | self.BOX_LEFT | self.BOX_RIGHT:
                # can we move this box?
                boxes_to_move = self.can_move_boxes(next_location, direction)
                if boxes_to_move:
                    print(boxes_to_move)
                    self.move_boxes(boxes_to_move, direction)
                    self.move_robot(direction, next_location)
        self.map.print()

    def move_robot(self, direction, next_location):
        self.map.set_char(self.ROBOT, next_location)
        self.map.set_char(self.EMPTY, self.robot)
        self.robot += direction

    def move_boxes(self, boxes_to_move, direction: Vector):
        # sort this list descending in reverse direction order
        sorted_boxes: list[Vector] = []
        if direction == Vector.north():
            sorted_boxes = sorted(boxes_to_move, key=cmp_to_key(lambda a, b: a.row - b.row))
        elif direction == Vector.south():
            sorted_boxes = sorted(boxes_to_move, key=cmp_to_key(lambda a, b: a.row - b.row), reverse=True)
        elif direction == Vector.west():
            sorted_boxes = sorted(boxes_to_move, key=cmp_to_key(lambda a, b: a.col - b.col))
        elif direction == Vector.east():
            sorted_boxes = sorted(boxes_to_move, key=cmp_to_key(lambda a, b: a.col - b.col), reverse=True)

        print(sorted_boxes)
        # collect up all the box characters
        box_characters = []
        for box in sorted_boxes:
            box_characters.append(self.map.value(box))
        for i in range(len(sorted_boxes)):
            self.map.set_char(box_characters[i], sorted_boxes[i] + direction)
            self.map.set_char(self.EMPTY, sorted_boxes[i])

    @staticmethod
    def get_direction(instruction):
        direction = None
        match instruction:
            case '^':
                direction = Vector.north()
            case '<':
                direction = Vector.west()
            case '>':
                direction = Vector.east()
            case 'v':
                direction = Vector.south()
        return direction

    def can_move_boxes(self, location: Vector, direction: Vector) -> list[Vector] | None:
        """Checks to see if the box at the location can be moved in the given direction.

        Recursively tries to move an entire stack of boxes.

        Returns:
             None if the boxes would hit a wall, or the location of all movable boxes, in order of movability.
        """
        box_locations = []
        box = self.map.value(location)
        match box:
            case self.BOX:
                box_locations = [location]
            case self.BOX_LEFT:
                box_locations = [location, location + Vector.east()]
            case self.BOX_RIGHT:
                box_locations = [location + Vector.west(), location]
        if (box == self.BOX_LEFT and direction == Vector.east()) or (
                box == self.BOX_RIGHT and direction == Vector.west()):
            # don't look at the box itself next, skip over and look at the next location
            next_locations = [location + direction + direction]
        else:
            next_locations = [i + direction for i in box_locations]

        for next_location in next_locations:
            neighbor = self.map.value(next_location)
            match neighbor:
                case self.EMPTY:
                    # Empty space ahead, we're a free box, return
                    pass
                case self.WALL:
                    # Wall ahead, cannot move, return immediately
                    return None
                case self.BOX|self.BOX_LEFT|self.BOX_RIGHT:
                    # Box ahead, can that box move?
                    more_movable_boxes = self.can_move_boxes(next_location, direction)
                    if more_movable_boxes:
                        box_locations = more_movable_boxes + box_locations  # prepend
                    else:
                        return None
        return box_locations

    def gps_sum(self):
        boxes = self.map.find_all(self.BOX)
        boxes += self.map.find_all(self.BOX_LEFT)
        total = 0
        for box in boxes:
            total += 100 * box.row + box.col
        return total

    def scale_up(self):
        new_lines = []
        for line in self.map.map_string:
            new_line = ''
            for char in line:
                match char:
                    case self.BOX:
                        new_line += self.BOX_LEFT + self.BOX_RIGHT
                    case self.WALL:
                        new_line += self.WALL + self.WALL
                    case self.EMPTY:
                        new_line += self.EMPTY + self.EMPTY
                    case self.ROBOT:
                        new_line += self.ROBOT + self.EMPTY
                        self.robot.col = self.robot.col * 2
            new_lines.append(new_line)
        self.map = Map(new_lines)
