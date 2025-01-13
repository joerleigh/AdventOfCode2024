#! python3
from aoc import AdventOfCode


def is_lock(block):
    return block[0] == '#####'


def keys_and_locks(blocks: list[tuple[str,...]]):
    keys = []
    locks = []
    for block in blocks:
        heights = [0, 0, 0, 0, 0]
        if is_lock(block):
            for height in reversed(range(1,7)):
                for pin in range(5):
                    if heights[pin]==0 and block[height][pin] == '#':
                        heights[pin]=height
            locks.append(heights)
        else:
            for height in range(1,7):
                for pin in range(5):
                    if heights[pin]==0 and block[height][pin] == '#':
                        heights[pin]=6-height
            keys.append(heights)
    return keys, locks

def fits(key, lock):
    for pin in range(5):
        if key[pin]+lock[pin]>=6:
            return False
    return True


class Day25(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)

    def block(self, i):
        return tuple(self.input[i * 8:i * 8 + 7])

    def part_one(self):
        blocks = [self.block(i) for i in range(int((len(self.input) + 1) / 8))]
        keys, locks = keys_and_locks(blocks)
        total_fit = 0
        for key in keys:
            for lock in locks:
                if fits(key, lock):
                    total_fit += 1
        return total_fit