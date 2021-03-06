#!/usr/bin/env python3

# Day 2: Dive! (Part One)
# https://adventofcode.com/2021/day/2
# Henrique Rocha <henrique.rocha@protonmail.com>

# You can run this code by running:
# $ python3 day2_part1.py < input.txt

import sys
import day2_common

def move(submarine, direction, units):
    if direction == "forward":
        submarine.moveForward(units)
    elif direction == "down":
        submarine.moveDown(units)
    elif direction == "up":
        submarine.moveUp(units)

submarine = day2_common.Submarine()
for line in sys.stdin:
    (direction, units) = day2_common.parse_move(line)
    move(submarine, direction, units)

print(submarine.horizontal * submarine.depth)
