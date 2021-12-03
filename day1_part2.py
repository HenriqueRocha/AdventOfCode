#!/usr/bin/env python3

# Day 1: Sonar Sweep (Part Two)
# https://adventofcode.com/2021/day/1
# Henrique Rocha <henrique.rocha@protonmail.com>

# You can run this code by running:
# $ python3 day1_part2.py < input.txt

import sys
import queue

def init_sliding_window():
    sum = 0
    sliding_window = queue.SimpleQueue()
    for i in range(3):
        n = int(sys.stdin.readline())
        sum += n
        sliding_window.put(n)

    return (sliding_window, sum)


times_sums_increased = 0
(sliding_window, previous_measurements_sum) = init_sliding_window()

for line in sys.stdin:
    measurement = int(line)
    measurements_sum = previous_measurements_sum + measurement - sliding_window.get()
    sliding_window.put(measurement)
    if measurements_sum > previous_measurements_sum:
        times_sums_increased += 1
    previous_measurements_sum = measurements_sum

print(times_sums_increased)
