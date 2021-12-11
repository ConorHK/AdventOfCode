#!/usr/bin/env python3

increased_depth = 0

def compare_depth(depth, previous_depth):
    if depth > previous_depth:
        return 1
    return 0
    
with open("input.txt") as f:
    depths = [int(line) for line in f.readlines()]

previous_depth = 1000
for depth in depths:
    increased_depth += compare_depth(depth, previous_depth)
    previous_depth = depth
print(f"part one: {increased_depth}")

increased_depth = 0
for position, _ in enumerate(depths):
    window_a = depths[position : position + 3]
    position += 1
    window_b = depths[position : position + 3]
    increased_depth += compare_depth(sum(window_b), sum(window_a))
print(f"part two: {increased_depth}")
