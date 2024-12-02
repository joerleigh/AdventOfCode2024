#! python3

def part_one(file):
    firstlist, secondlist = read_lists(file)

    firstlist.sort()
    secondlist.sort()

    total = 0
    for i in range(len(firstlist)):
        total += abs(firstlist[i]-secondlist[i])

    print(total)

def part_two(file):
    firstlist, secondlist = read_lists(file)

    total = 0
    for first in firstlist:
        found = 0
        for second in secondlist:
            if first == second:
                found+=1
        total += first * found
    print(total)

def read_lists(file):
    firstlist = []
    secondlist = []
    while line := file.readline():
        numbers = line.split()
        firstlist.append(int(numbers[0]))
        secondlist.append(int(numbers[1]))
    return firstlist, secondlist

