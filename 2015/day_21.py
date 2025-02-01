from __future__ import annotations

import itertools
import math

from aoc import AdventOfCode


class Item:
    def __init__(self, name, cost, damage, defense):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.defense = defense

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Fighter:
    def __init__(self, health: int):
        self.health = health

    def damage(self) -> int:
        pass

    def defense(self) -> int:
        pass

    def turns_to_die(self, attacker: Fighter) -> int:
        return math.ceil(self.health / max(attacker.damage() - self.defense(), 1)) # todo this calculation is wrong, somehow


class Player(Fighter):
    def __init__(self, health: int, weapon: Item, armor: Item, rings: tuple[Item, Item]):
        super().__init__(health)
        self.weapon = weapon
        self.armor = armor
        self.rings = rings

    def damage(self) -> int:
        return self.weapon.damage + self.rings[0].damage + self.rings[1].damage

    def defense(self) -> int:
        return self.armor.defense + self.rings[0].defense + self.rings[1].defense

    def gear_cost(self) -> int:
        return self.weapon.cost + self.armor.cost + self.rings[0].cost + self.rings[1].cost


class Boss(Fighter):
    def __init__(self, health: int, damage: int, defense: int):
        super().__init__(health)
        self.damage_val = damage
        self.defense_val = defense

    def damage(self) -> int:
        return self.damage_val

    def defense(self) -> int:
        return self.defense_val


def simulate(player: Fighter, boss: Fighter, verbose: int = 0) -> bool:
    """Returns true if player wins"""

    player_health = player.health
    boss_health = boss.health
    turns = 1
    while True:
        boss_health -= max(1, player.damage() - boss.defense())
        if verbose > 1:
            print(f'Player deals {max(1, player.damage() - boss.defense())} damage, boss has {boss_health}')
        if boss_health <= 0:
            if verbose > 0:
                print(f'Player wins in {turns} turns')
            return True
        player_health -= max(1, boss.damage() - player.defense())
        if verbose > 1:
            print(f'Boss deals {max(1, boss.damage() - player.defense())} damage, player has {player_health}')
        if player_health <= 0:
            if verbose > 0:
                print(f'Player dies in {turns} turns')
            return False
        turns += 1


class Day21(AdventOfCode):
    """Advent of Code 2015 Day 21

    https://adventofcode.com/2015/day/21"""

    weapons = [
        Item('Dagger', 8, 4, 0),
        Item('Shortsword', 10, 5, 0),
        Item('Warhammer', 25, 6, 0),
        Item('Longsword', 40, 7, 0),
        Item('Greataxe', 74, 8, 0)
    ]
    armor = [
        Item('No armor', 0, 0, 0),
        Item('Leather', 13, 0, 1),
        Item('Chainmail', 31, 0, 2),
        Item('Splintmail', 53, 0, 3),
        Item('Bandedmail', 75, 0, 4),
        Item('Platemail', 102, 0, 5)
    ]
    rings = [
        Item('No ring', 0, 0, 0),
        Item('No ring', 0, 0, 0),
        Item('Damage +1', 25, 1, 0),
        Item('Damage +2', 50, 2, 0),
        Item('Damage +3', 100, 3, 0),
        Item('Defense +1', 20, 0, 1),
        Item('Defense +2', 40, 0, 2),
        Item('Defense +3', 80, 0, 3)
    ]

    def __init__(self, file):
        super().__init__(file)
        self.player_cache = {}

    def gear_combos(self):
        for weapon in self.weapons:
            for armor in self.armor:
                for rings in itertools.combinations(self.rings, 2):
                    yield weapon, armor, rings

    def part_one(self):
        """You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of
        gold you can spend and still win the fight?"""

        # calculate min gold for each attack, defense rating
        for weapon, armor, rings in self.gear_combos():
            player = Player(100, weapon, armor, rings)
            player_defense = player.defense()
            if player_defense not in self.player_cache:
                self.player_cache[player_defense] = {}
            player_damage = player.damage()
            if player_damage not in self.player_cache[player_defense]:
                self.player_cache[player_defense][player_damage] = player
            elif player.gear_cost() < self.player_cache[player_defense][player_damage].gear_cost():
                self.player_cache[player_defense][player_damage] = player

        # Defense can be anything from 0-8. The number of turns the player will survive is based only on their
        # defense. Calculate that for each level of defense, then find the minimum damage required to kill the boss
        # in at most n+1 turns. Then find the min cost to reach that level of defense, plus the min cost to reach
        # that level of damage. Then figure out the minimum of those costs.
        boss_health = int(self.input[0].split(': ')[1])
        boss_damage = int(self.input[1].split(': ')[1])
        boss_defense = int(self.input[2].split(': ')[1])
        boss = Boss(boss_health, boss_damage, boss_defense)
        min_cost = None
        for defense in self.player_cache.keys():
            dummy = Boss(100, 0, defense)
            turns = dummy.turns_to_die(boss)
            min_damage = math.ceil(boss.health / (turns + 1)) + boss.defense()
            print(f'{defense} defense, {turns} turns to die, need to do {min_damage} damage')
            cost = None
            for damage in range(min_damage, 15):
                if damage in self.player_cache[defense]:
                    player = self.player_cache[defense][damage]
                    cost = player.gear_cost()
                    print(f'\t{cost} gold: {player.weapon}, {player.armor}, {player.rings}')
                    print(f'\t{player.damage()} damage, {player.defense()} defense')
                    print(f'\t{boss.turns_to_die(player)} turns to beat')
                    simulate(player, boss, 1)
                    break
            if cost is not None:
                min_cost = min(cost, min_cost) if min_cost is not None else cost
        print(f'Min cost to beat: {min_cost}')

        print('----------')

        min_cost = None
        for weapon, armor, rings in self.gear_combos():
            player = Player(100, weapon, armor, rings)
            cost = player.gear_cost()
            if min_cost is None or cost < min_cost:
                if simulate(player, boss):
                    print(f'{cost} gold: {player.weapon}, {player.armor}, {player.rings}')
                    simulate(player, boss, 1)
                    min_cost = cost

    def part_two(self):
        boss_health = int(self.input[0].split(': ')[1])
        boss_damage = int(self.input[1].split(': ')[1])
        boss_defense = int(self.input[2].split(': ')[1])
        boss = Boss(boss_health, boss_damage, boss_defense)

        max_cost = None
        for weapon, armor, rings in self.gear_combos():
            player = Player(100, weapon, armor, rings)
            cost = player.gear_cost()
            if max_cost is None or cost > max_cost:
                if not simulate(player, boss):
                    print(f'{cost} gold: {player.weapon}, {player.armor}, {player.rings}')
                    simulate(player, boss, 1)
                    max_cost = cost
