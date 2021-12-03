#!/usr/bin/env python3

# Day 1: Sonar Sweep (Part One)
# https://adventofcode.com/2021/day/1
# Henrique Rocha <henrique.rocha@protonmail.com>

# You can run this code by running:
# $ python3 day1_part1.py < input.txt

import sys

times_depth_increased = 0
previous_measurement = int(sys.stdin.readline())

for line in sys.stdin:
    measurement = int(line)
    if measurement > previous_measurement:
        times_depth_increased += 1
    previous_measurement = measurement

print(times_depth_increased)
