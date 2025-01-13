#! python3

def part_one(file):
    totalsafe = 0
    while line := file.readline():
        levels = line.split()
        safe = test_levels(levels)

        if safe:
            totalsafe += 1

    return totalsafe

def part_two(file):
    totalsafe = 0
    while line := file.readline():
        levels = line.split()
        safe = test_levels(levels)

        if safe:
            totalsafe += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[0:i]+levels[i+1:]
                safe = test_levels(new_levels)
                if safe:
                    totalsafe += 1
                    break
    return totalsafe

def test_levels(levels):
    increasing = None
    safe = True
    previous = 0
    for i in range(len(levels)):
        if i > 0:
            diff = int(levels[i]) - previous
            if abs(diff) > 3 or not (
                    increasing is None or (increasing and diff > 0) or (not increasing and diff < 0)):
                safe = False
                break
            if diff > 0:
                increasing = True
            elif diff < 0:
                increasing = False
            else:
                safe = False
                break
        previous = int(levels[i])
    return safe
