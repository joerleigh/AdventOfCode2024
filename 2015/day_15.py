from __future__ import annotations

from aoc import AdventOfCode
import re


class Day15(AdventOfCode):
    """Advent of Code 2015 Day 15
    
    https://adventofcode.com/2015/day/15"""

    def __init__(self, file):
        super().__init__(file)

    def part_one(self):
        ingredients = []
        for line in self.input:
            match = re.search(
                r'^([a-z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)',
                line, re.I | re.M)
            ingredients.append(Ingredient(int(match[2]), int(match[3]), int(match[4]), int(match[5]), int(match[6])))
        permutations = self.permutations(100, len(ingredients))
        max_score = 0
        for permutation in permutations:
            score = self.score([(ingredients[i], permutation[i]) for i in range(len(ingredients))])
            max_score = max(max_score, score)
        print(max_score)

    def part_two(self):
        ingredients = []
        for line in self.input:
            match = re.search(
                r'^([a-z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)',
                line, re.I | re.M)
            ingredients.append(Ingredient(int(match[2]), int(match[3]), int(match[4]), int(match[5]), int(match[6])))
        permutations = self.permutations(100, len(ingredients))
        max_score = 0
        for permutation in permutations:
            ingredient_list = [(ingredients[i], permutation[i]) for i in range(len(ingredients))]
            if self.calories(ingredient_list) == 500:
                score = self.score(ingredient_list)
                max_score = max(max_score, score)
        print(max_score)

    @staticmethod
    def score(ingredients: list[tuple[Ingredient, int]]):
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        for ingredient, amount in ingredients:
            capacity += amount * ingredient.capacity
            durability += amount * ingredient.durability
            flavor += amount * ingredient.flavor
            texture += amount * ingredient.texture
        return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

    @staticmethod
    def calories(ingredients: list[tuple[Ingredient, int]]):
        calories = 0
        for ingredient, amount in ingredients:
            calories += amount * ingredient.calories
        return calories

    def permutations(self, total, num):
        if num == 1:
            return [(total,)]
        all_perms = []
        for i in range(total + 1):
            later_perms = self.permutations(total - i, num - 1)
            all_perms += [(i, *perm) for perm in later_perms]
        return all_perms


class Ingredient:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
