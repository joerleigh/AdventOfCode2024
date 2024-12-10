#! python3
from aoc import AdventOfCode


class Day9(AdventOfCode):
    def part_one(self) -> int:
        disk_blocks = self.parse_disk_blocks()
        self.compact_blocks(disk_blocks)
        return self.checksum(disk_blocks)

    def part_two(self) -> int:
        disk_blocks = self.parse_disk_blocks()
        self.compact_files(disk_blocks)
        return self.checksum(disk_blocks)

    def parse_disk_blocks(self):
        is_file = True
        file_num = 0
        disk_blocks = []
        for size in self.input[0]:  # input is just one line
            size = int(size)
            block_id = None
            if is_file:
                block_id = file_num
                file_num += 1
            for i in range(size):
                disk_blocks.append(block_id)
            is_file = not is_file
        return disk_blocks

    def compact_blocks(self, disk_blocks):
        for i in reversed(range(len(disk_blocks))):
            if disk_blocks[i] is not None:  # skip already empty blocks
                first_empty_block = None
                for j in range(i):  # find the first empty block
                    if disk_blocks[j] is None:
                        first_empty_block = j
                        break
                if first_empty_block is None:  # found no empty blocks, we're fully compact
                    break
                disk_blocks[first_empty_block] = disk_blocks[i]
                disk_blocks[i] = None

    def compact_files(self, disk_blocks):
        current_file = None
        file_end = None
        for i in reversed(range(len(disk_blocks))):
            if current_file is None:
                current_file = disk_blocks[i]
                file_end = i
            elif current_file != disk_blocks[i]:
                # we found a whole file
                file_size = file_end-i
                file_start = i+1
                # look for a gap at least that size, starting from the beginning
                gap_start = None
                gap_size = 0
                for j in range(i+2): #i+2 is the postion of the start of the file, which lets us find a gap just before the file
                    if disk_blocks[j] is None:
                        if gap_start is None:
                            gap_start = j
                    else:
                        if gap_start is not None:
                            gap_size = j-gap_start
                            if gap_size >= file_size:
                                break
                            gap_start = None
                            gap_size = 0
                # move the file into the gap, if found
                if gap_start is not None and gap_size >= file_size:
                    for j in range(file_size):
                        disk_blocks[gap_start+j] = disk_blocks[file_start+j]
                        disk_blocks[file_start+j] = None
                # finally, start the search again
                current_file = disk_blocks[i]
                file_end = i

    def checksum(self, disk_blocks):
        checksum = 0
        for i in range(len(disk_blocks)):
            if disk_blocks[i] is None:
                continue
            checksum += i * disk_blocks[i]
        return checksum
