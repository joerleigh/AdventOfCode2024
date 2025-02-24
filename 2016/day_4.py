from aoc import AdventOfCode
import re


class Day4(AdventOfCode):
    """Advent of Code 2016 Day 4
    
    https://adventofcode.com/2016/day/4"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        id_total = 0
        for line in self.input:
            result = re.search(r'^([a-z\-]+)(\d+)\[([a-z]{5})]', line)
            room_code = result[1]
            room_id = int(result[2])
            checksum = result[3]

            # Aggregate character frequency from room code
            char_freq = {}
            for char in room_code:
                if char != '-':
                    if char not in char_freq:
                        char_freq[char] = 0
                    char_freq[char] += 1

            # Compute checksum for room code
            computed_checksum = ""
            while True:
                max_freq = max(char_freq.values())
                max_chars = [i[0] for i in char_freq.items() if i[1] == max_freq]
                max_chars.sort()
                for c in max_chars:
                    computed_checksum += c
                    del char_freq[c]
                    if len(computed_checksum) == 5:
                        break
                if len(computed_checksum) == 5:
                    break

            if checksum == computed_checksum:
                id_total += room_id

        print(id_total)

    def part_two(self):
        for line in self.input:
            result = re.search(r'^([a-z\-]+)(\d+)\[([a-z]{5})]', line)
            room_code = result[1]
            room_id = int(result[2])
            checksum = result[3]

            decoded_room_name = ''
            for char in room_code:
                if char != '-':
                    char_num = ord(char) - 97
                    char_num += room_id
                    char_num %= 26
                    char_num += 97
                    decoded_room_name += chr(char_num)
                else:
                    decoded_room_name+=' '
            if decoded_room_name.find('north') != -1:
                print(decoded_room_name, room_id)
