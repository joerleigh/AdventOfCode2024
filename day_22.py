#! python3
from aoc import AdventOfCode
from functools import cache


@cache
def next_secret(secret: int):
    """Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number.
    Finally, prune the secret number.

    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then,
    mix this result into the secret number. Finally, prune the secret number.

    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number.
    Finally, prune the secret number."""

    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, int(secret / 32)))
    secret = prune(mix(secret, secret * 2048))
    return secret


def mix(secret, value):
    """To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number.
    Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15
    into the secret number, the secret number would become 37.)"""

    return secret ^ value


def prune(secret):
    """To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number
    becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number,
    the secret number would become 16113920.)"""

    return secret % 16777216




class Day22(AdventOfCode):
    def __init__(self, file):
        super().__init__(file)
        self.values = None

    @cache
    def find_total_value(self, four_changes):
        total = 0
        for secret_num in range(len(self.values)):
            if four_changes in self.values[secret_num]:
                total += self.values[secret_num][four_changes]
        return total

    def part_one(self):
        total = 0
        for secret in self.input:
            secret = int(secret)
            original_secret = secret
            for i in range(2000):
                secret = next_secret(secret)
            print(f'{original_secret}: {secret}')
            total += secret
        return total

    def part_two(self):
        self.values = []
        for secret_num in range(len(self.input)):
            secret = int(self.input[secret_num])
            self.values.append({})
            previous_price = secret % 10
            change_2 = None
            change_3 = None
            change_4 = None
            for i in range(2000):
                secret = next_secret(secret)
                price = secret % 10
                change_1 = price - previous_price
                previous_price = price

                if change_4 is not None and (change_4, change_3, change_2, change_1) not in self.values[secret_num]:
                    self.values[secret_num][(change_4, change_3, change_2, change_1)] = price

                change_4 = change_3
                change_3 = change_2
                change_2 = change_1

        # loop through all sets of four price changes and calculate the total price for each, i guess
        max_value = 0
        for secret_num in range(len(self.values)):
            for last_four in self.values[secret_num].keys():
                found_value = self.find_total_value(last_four)
                if max_value < found_value:
                    max_value = found_value
                    print(f'New max {last_four} (list {secret_num}): {found_value}')
        return max_value
