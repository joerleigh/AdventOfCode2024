#! python3
from __future__ import annotations

import configparser
import importlib
import os
import shutil
import urllib.request
from typing import Literal, Any


class AdventOfCode:
    ALPHANUMERIC = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, lines: list[str]):
        self.input: list[str] = lines

    def part_one(self, *args):
        pass

    def part_two(self, *args):
        pass

    def run(self, part: Literal[1, 2], *args):
        if part == 1:
            return self.part_one(*args)
        elif part == 2:
            return self.part_two(*args)
        return None


def run_day(year: int, day: int, part: Literal[1, 2], use_sample: bool, *args):
    filename = input_filename(year, day, part, use_sample)

    modulename = f'{year}.day_{day}'
    day_module = importlib.import_module(modulename)

    class_name = f'Day{day}'
    class_ = getattr(day_module, class_name)
    print(f'Loading year {year} day {day}, part {part} from {class_name} class')
    with open(filename) as file:
        day_class: AdventOfCode = class_([line.strip() for line in file.readlines()])
        return day_class.run(part, *args)


def input_filename(year, day, part=1, use_sample=False):
    suffix = '_sample' if use_sample else ''
    filename = f'{year}/inputs/day_{day}_{part}{suffix}.txt'
    if not os.path.isfile(filename):
        filename = f'{year}/inputs/day_{day}{suffix}.txt'
    return filename


def code_filename(year, day):
    return f"{year}/day_{day}.py"


def download_day(year, day):
    """
    Downloads a challenge from AoC.
    The url pattern is as follow:
    https://adventofcode.com/2020/day/1/input
    The header should contain a session cookie.
    """

    session_cookie = load_config()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    filename = input_filename(year, day)

    request = urllib.request.Request(url)
    request.add_header("Cookie", f"session={session_cookie}")

    print(url)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with urllib.request.urlopen(request) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    # create an empty sample file, too
    filename = input_filename(year, day, use_sample=True)
    open(filename, 'a').close()


def template_day(year, day):
    filename = code_filename(year, day)
    if not os.path.exists(filename):
        tpl = get_template(year, day)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write(tpl)


def get_template(year, day):
    return f"""from aoc import AdventOfCode
        
class Day{day}(AdventOfCode):
    \"""Advent of Code {year} Day {day}
    
    https://adventofcode.com/{year}/day/{day}\"""
    
    def __init__(self, file):
        super().__init__(file)
    
    def part_one(self):
        pass
        
    def part_two(self):
        pass
    """


def load_config(filename: str = "settings.ini"):
    config = configparser.ConfigParser()
    config.read(filename)

    return config["settings"]["session"]
