from copy import copy, deepcopy

from aoc import AdventOfCode
from dataclasses import dataclass


@dataclass
class Spell:
    name: str
    cost: int
    damage: int = 0
    heal: int = 0
    recharge: int = 0
    armor: int = 0
    duration: int = 0
    cast_message: str = ''
    effect_message: str = ''


class Day22(AdventOfCode):
    """Advent of Code 2015 Day 22
    
    https://adventofcode.com/2015/day/22"""

    def __init__(self, file):
        super().__init__(file)
        self.boss_health = int(self.input[0].split(': ')[1])
        self.boss_damage = int(self.input[1].split(': ')[1])
        self.player_health = int(self.input[2].split(': ')[1])
        self.player_mana = int(self.input[3].split(': ')[1])
        self.min_spent_to_win = None
        self.min_spells = None

    available_spells = [
        Spell('Magic Missile', 53, damage=4, cast_message='dealing 4 damage'),
        Spell('Drain', 73, damage=2, heal=2, cast_message='dealing 2 damage, and healing 2 hit points'),
        Spell('Shield', 113, armor=7, duration=6, cast_message='increasing armor by 7'),
        Spell('Poison', 173, damage=3, duration=6, effect_message='deals 3 damage'),
        Spell('Recharge', 229, recharge=101, duration=5, effect_message='provides 101 mana'),
    ]

    def play(self, player_health: int, player_mana: int, boss_health: int, spell_stack: list[Spell], mana_spent: int,
             player_turn: bool, turns: list[Spell], hard_mode: bool = False):
        # In hard mode, you lose 1hp per player turn
        if player_turn and hard_mode:
            player_health -= 1

        # check if the player is dead and return
        if player_health < 1:
            return False

        active_armor = 0
        # Apply all spell effects on the stack, decrease all durations by 1
        for spell in spell_stack:
            boss_health -= spell.damage
            player_health += spell.heal
            player_mana += spell.recharge
            active_armor += spell.armor
            spell.duration -= 1
        # Remove any spells whose durations have hit 0
        pruned_spell_stack = [s for s in spell_stack if s.duration > 0]

        # Check if the boss are dead and return
        if boss_health < 1:
            # If the boss is dead, set self.min_spent_to_win
            if self.min_spent_to_win is None or mana_spent < self.min_spent_to_win:
                self.min_spent_to_win = mana_spent
                self.min_spells = turns
            return True
        # Check if the current spent mana is greater than self.min_spent_to_win and give up if so
        if self.min_spent_to_win is not None and mana_spent >= self.min_spent_to_win:
            return False

        # if player's turn:
        if player_turn:
            #  for all affordable spells, try to cast that spell and recurse
            affordable_spells = [s for s in self.available_spells if
                                 s.cost <= player_mana and s.name not in [ss.name for ss in pruned_spell_stack]]
            if affordable_spells:
                for spell in affordable_spells:
                    #  spells with duration 0 get applied instantly, otherwise get added to the stack
                    self.play(
                        (player_health + spell.heal) if spell.duration == 0 else player_health,
                        (player_mana - spell.cost + spell.recharge) if spell.duration == 0 else (
                                player_mana - spell.cost),
                        (boss_health - spell.damage) if spell.duration == 0 else boss_health,
                        deepcopy(pruned_spell_stack) if spell.duration == 0 else (
                                deepcopy(pruned_spell_stack) + [deepcopy(spell)]),
                        mana_spent + spell.cost,
                        False,
                        turns + [spell],
                        hard_mode
                    )
        # if boss's turn:
        else:
            # boss deals damage minus any active armor, with min damage 1
            #  recurse again
            self.play(
                player_health - max(self.boss_damage - active_armor, 1),
                player_mana,
                boss_health,
                deepcopy(pruned_spell_stack),
                mana_spent,
                True,
                turns,
                hard_mode
            )

    def part_one(self):
        self.play(self.player_health, self.player_mana, self.boss_health, [], 0, True, [])
        print(self.min_spent_to_win)
        self.simulate(self.player_health, self.player_mana, self.boss_health, [], 0, True, self.min_spells)

    def part_two(self):
        self.play(self.player_health, self.player_mana, self.boss_health, [], 0, True, [], True)
        print(self.min_spent_to_win)
        self.simulate(self.player_health, self.player_mana, self.boss_health, [], 0, True, self.min_spells, True)

    def simulate(self, player_health: int, player_mana: int, boss_health: int, spell_stack: list[Spell],
                 mana_spent: int,
                 player_turn: bool, turns: list[Spell], hard_mode: bool = False):
        if len(turns) == 0 and player_turn:
            return
        print(f'-- {"Player" if player_turn else "Boss"} turn --')
        print(f'- Player has {player_health} hit points, {player_mana} mana')
        print(f'- Boss has {boss_health} hit points')
        # In hard mode, you lose 1hp per player turn
        if player_turn and hard_mode:
            print('Player loses 1 health from hard mode.')
            player_health -= 1

        active_armor = 0
        # Apply all spell effects on the stack, decrease all durations by 1
        for spell in spell_stack:
            boss_health -= spell.damage
            player_health += spell.heal
            player_mana += spell.recharge
            active_armor += spell.armor
            spell.duration -= 1
            if len(spell.effect_message)>0:
                print(f'{spell.name} {spell.effect_message}; its timer is now {spell.duration}.')
            else:
                print(f'{spell.name}\'s timer is now {spell.duration}')
        # Remove any spells whose durations have hit 0
        pruned_spell_stack = [s for s in spell_stack if s.duration > 0]

        # if player's turn:
        if player_turn:
            spell = turns[0]
            print(f'Player casts {spell.name}' + (f', {spell.cast_message}.' if len(spell.cast_message) > 0 else '.'))
            print()
            #  spells with duration 0 get applied instantly, otherwise get added to the stack
            self.simulate(
                (player_health + spell.heal) if spell.duration == 0 else player_health,
                (player_mana - spell.cost + spell.recharge) if spell.duration == 0 else (
                        player_mana - spell.cost),
                (boss_health - spell.damage) if spell.duration == 0 else boss_health,
                deepcopy(pruned_spell_stack) if spell.duration == 0 else (
                        deepcopy(pruned_spell_stack) + [deepcopy(spell)]),
                mana_spent + spell.cost,
                False,
                turns[1:],
                hard_mode
            )
        # if boss's turn:
        else:
            # boss deals damage minus any active armor, with min damage 1
            print(f'Boss attacks for {max(self.boss_damage - active_armor, 1)} damage!')
            print()
            #  recurse again
            self.simulate(
                player_health - max(self.boss_damage - active_armor, 1),
                player_mana,
                boss_health,
                deepcopy(pruned_spell_stack),
                mana_spent,
                True,
                turns,
                hard_mode
            )
