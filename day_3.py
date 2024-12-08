#! python3
import re

def part_one(file):
    total = 0
    while line:= file.readline():
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line, re.S | re.M)
        for match in matches:
            total += int(match[0])*int(match[1])
    return total

def part_two(file):
    enabled = True
    total = 0
    while line:=file.readline():
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', line, re.S | re.M)
        for match in matches:
            if match[2] != '':
                enabled = True
            elif match[3] != '':
                enabled = False
            elif enabled:
                total += int(match[0])*int(match[1])
    return total