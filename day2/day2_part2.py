#!/usr/bin/env python3

# Day 2: Dive! (Part Two)
# https://adventofcode.com/2021/day/2
# Henrique Rocha <henrique.rocha@protonmail.com>

# You can run this code by running:
# $ python3 day2_part2.py < input.txt

import sys
import day2_common

def move(submarine, direction, units):
    if direction == "forward":
        submarine.moveForward(units)
        submarine.moveDown(submarine.aim * units)
    elif direction == "down":
        submarine.increaseAim(units)
    elif direction == "up":
        submarine.decreaseAim(units)

submarine = day2_common.Submarine()

for line in sys.stdin:
    (direction, units) = day2_common.parse_move(line)
    move(submarine, direction, units)

print(submarine.horizontal * submarine.depth)
