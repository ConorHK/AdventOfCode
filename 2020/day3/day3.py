#!/usr/bin/env python3
from math import prod

def part_1(data):
    return trees_on_slope(data, 3, 1)

def part_2(data):
    return prod(trees_on_slope(data, dx, dy) for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

def trees_on_slope(data, dx, dy):
    return sum(line[(i * dx) % len(line)] == "#" for i, line in enumerate(data[::dy]))

with open('day3_input.txt') as f:
    inp = f.read().splitlines()
print("Part 1: " + str(part_1(inp)))
print("Part 2: " + str(part_2(inp)))

print(inp[::2])
