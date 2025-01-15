from time import struct_time

from aoc import AdventOfCode
import re


class Day11(AdventOfCode):
    """Advent of Code 2015 Day 11
    
    https://adventofcode.com/2015/day/11"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        password = self.input[0]
        self.find_next_password(password)

    def part_two(self):
        password = self.input[0]
        password = self.find_next_password(password)
        self.find_next_password(password)

    def find_next_password(self, password):
        while True:
            password = self.increment_password(password)
            if self.no_confusing_letters(password) \
                    and self.increasing_straight(password) \
                    and self.two_different_pairs(password):
                print(f'Found password: {password}')
                return password

    def increment_password(self, password):
        return self.increment_char(password, 7)

    def increment_char(self, password, i):
        if i < 0 or i >= len(password):
            return password
        char = password[i]
        char = chr(ord(char) + 1)
        if char == '{':  # the character after z
            char = 'a'
            password = password[:i] + char + password[i + 1:]
            return self.increment_char(password, i - 1)
        else:
            password = password[:i] + char + password[i + 1:]
            return password

    @staticmethod
    def no_confusing_letters(password: str):
        return password.find('i') == -1 and password.find('o') == -1 and password.find('l') == -1

    @staticmethod
    def increasing_straight(password):
        for i in range(len(password)-2):
            if ord(password[i])+1 == ord(password[i+1]) and ord(password[i+1])+1 == ord(password[i+2]):
                return True
        return False

    @staticmethod
    def two_different_pairs(password):
        return len(re.findall(r'([a-z])\1+', password)) >= 2
