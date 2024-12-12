#! python3
from typing import List

from aoc import AdventOfCode
import math


class Day11(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.stones = self.input[0].split()
        self.stone_cache = {}
        self.blink_cache = {}
        self.warmup_cache()

    def part_one(self) -> int:
        print(self.stones)
        for i in range(10):
            print(f'blink {i}')
            self.blink()
            print(self.stones)
        return len(self.stones)

    def part_two(self) -> int:
        for i in range(75):
            self.smarter_blink()
        return self.total_stones()

    def blink(self):
        newstones = []
        for stone in self.stones:
            newstones += self.new_stones(int(stone))
        self.stones = newstones

    @staticmethod
    def new_stones(stone:int):
        if stone == 0:
            return [1]
        digits = int(math.log10(stone)) + 1
        if digits % 2 == 0:
            return [int(str(stone)[:int(digits / 2)]), int(str(stone)[int(digits / 2):])]
        return [stone * 2024]

    def smarter_blink(self):
        old_stone_cache = self.stone_cache.copy()
        for stone in old_stone_cache:
            num_stones = old_stone_cache[stone]
            if num_stones > 0:
                new_stones = self.lookup_in_blink_cache(stone)
                if new_stones is None:
                    new_stones = self.new_stones(stone)
                    self.add_to_blink_cache(stone, new_stones)
                self.decrement_cache(stone, num_stones)
                for new_stone in new_stones:
                    self.increment_cache(new_stone, num_stones)

    def warmup_cache(self):
        for stone in self.stones:
            self.increment_cache(int(stone), 1)

    def increment_cache(self, stone: int, num: int):
        if not stone in self.stone_cache:
            self.stone_cache[stone] = 0
        self.stone_cache[stone] += num

    def decrement_cache(self, stone: int, num: int):
        self.stone_cache[stone] -= num

    def total_stones(self):
        total = 0
        for stone in self.stone_cache:
            total += self.stone_cache[stone]
        return total

    def lookup_in_blink_cache(self, stone) -> List[int] | None:
        if stone in self.blink_cache:
            return self.blink_cache[stone]
        return None

    def add_to_blink_cache(self, stone: int, new_stones: List[int]):
        if not stone in self.blink_cache:
            self.blink_cache[stone] = new_stones