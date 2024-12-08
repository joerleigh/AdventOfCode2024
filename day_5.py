#! python3
from functools import cmp_to_key, partial


def part_one(file):
    orders, rules = parse(file)

    total = 0
    for pages in orders:
        broke_rule = order_is_invalid(pages, rules)
        if not broke_rule:
            middle_index = int((len(pages) - 1) / 2)
            total += int(pages[middle_index])
    return total


def part_two(file):
    orders, rules = parse(file)

    total = 0
    for pages in orders:
        broke_rule = order_is_invalid(pages, rules)
        if broke_rule:
            pages = reorder_pages(pages, rules)
            middle_index = int((len(pages) - 1) / 2)
            total += int(pages[middle_index])
    return total


def reorder_pages(pages, rules):
    valid_rules = []
    for rule in rules:
        try:
            pages.index(rule[0])
            pages.index(rule[1])
        except ValueError:
            continue
        valid_rules.append(rule)
    return sorted(pages, key=cmp_to_key(partial(compare_by_rules, rules=valid_rules)))


def compare_by_rules(page1, page2, rules):
    for rule in rules:
        try:
            index1 = rule.index(page1)
            index2 = rule.index(page2)
        except ValueError:
            continue
        if index1 < index2:
            return -1
        elif index2 > index1:
            return 1
        else:
            return 0


def parse(file):
    parsing_rules = True
    rules = []
    orders = []
    while line := file.readline():
        line = line.strip()
        if parsing_rules:
            if line == "":
                parsing_rules = False
                continue
            rules.append(line.split('|'))
        else:
            orders.append(line.split(','))
    return orders, rules


def order_is_invalid(pages, rules):
    broke_rule = False
    for rule in rules:
        try:
            index1 = pages.index(rule[0])
            index2 = pages.index(rule[1])
        except ValueError:
            continue
        if index1 > index2:
            broke_rule = True
            break
    return broke_rule
