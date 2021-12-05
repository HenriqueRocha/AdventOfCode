#!/usr/bin/env python3

# Day 3: Binary Diagnostic! (Part One)
# https://adventofcode.com/2021/day/2
# Henrique Rocha <henrique.rocha@protonmail.com>

# You can run this code by running:
# $ python3 day2_part1.py < input.txt

import sys

def compute_gamma_epsilon_rates(one_counts, n_numbers):
    gamma = []
    epsilon = []
    for count in one_counts:
        if count < n_numbers / 2:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
    return (gamma, epsilon)

def convert_to_decimal(bit_list):
    result = 0
    n_bits = len(bit_list) - 1
    for bit in bit_list:
        result += bit * (2 ** n_bits)
        n_bits -= 1
    return result

binary_number = sys.stdin.readline().rstrip()
n_bits = len(binary_number)
one_counts = [0] * n_bits
n_numbers = 1

for line in sys.stdin:
    for i in range(n_bits):
        one_counts[i] += int(line[i])
    n_numbers += 1

(gamma, epsilon) = compute_gamma_epsilon_rates(one_counts, n_numbers)

power_consumption = convert_to_decimal(gamma) * convert_to_decimal(epsilon)
print(power_consumption)

    
