#!/usr/bin/env python3

# Day 2: Dive! (Part One)
# https://adventofcode.com/2021/day/2
# Henrique Rocha <henrique.rocha@protonmail.com>

# You can run this code by running:
# $ python3 day2_part1.py < input.txt

import sys

def parse_move(s):
    split = s.split()
    return (split[0], int(split[1]))

def move(x, z, direction, units):
    if direction == "forward":
        return (x + units, z)
    elif direction == "down":
        return (x, z + units)
    elif direction == "up":
        return (x, z - units)

horizontal = 0
depth = 0

for line in sys.stdin:
    (direction, units) = parse_move(line)
    (horizontal, depth) = move(horizontal, depth, direction, units)

print(horizontal * depth)
