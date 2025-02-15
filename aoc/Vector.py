from __future__ import annotations


class Vector:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col

    @classmethod
    def north(cls):
        return cls(-1, 0)

    @classmethod
    def east(cls):
        return cls(0, 1)

    @classmethod
    def south(cls):
        return cls(1, 0)

    @classmethod
    def west(cls):
        return cls(0, -1)

    @classmethod
    def turn_right(cls, facing) -> Vector:
        if facing == cls.north():
            return cls.east()
        elif facing == cls.east():
            return cls.south()
        elif facing == cls.south():
            return cls.west()
        else:
            return cls.north()

    @classmethod
    def turn_left(cls, facing) -> Vector:
        if facing == cls.north():
            return cls.west()
        elif facing == cls.east():
            return cls.north()
        elif facing == cls.south():
            return cls.east()
        else:
            return cls.south()

    @classmethod
    def cardinal_directions(cls) -> list[Vector]:
        return [cls.north(), cls.east(), cls.south(), cls.west()]

    def __add__(self, other) -> Vector:
        return Vector(self.row + other.row, self.col + other.col)

    def __sub__(self, other) -> Vector:
        return Vector(self.row - other.row, self.col - other.col)

    def __mul__(self, other) -> Vector:
        return Vector(self.row * other, self.col * other)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.row == other.row and self.col == other.col

    def __str__(self) -> str:
        return f'[{self.row},{self.col}]'

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.row, self.col))
