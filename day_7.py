#! python3

def part_one(file):
    total = find_solutions(file, [add, mult])
    print(total)


def part_two(file):
    total = find_solutions(file, [add, mult, concat])
    print(total)


def find_solutions(file, operators):
    total = 0
    while line := file.readline():
        value, number_str = line.split(': ')
        value = int(value)
        numbers = number_str.split()
        if adds_up(int(numbers[0]), numbers[1:], value, operators):
            total += value
    return total


def adds_up(accumulator, numbers, value, operators):
    if len(numbers) == 0:
        return accumulator == value
    for operator in operators:
        if adds_up(operator(accumulator, int(numbers[0])), numbers[1:], value, operators):
            return True
    return False


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))
