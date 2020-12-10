#!/usr/bin/env python3
from collections import defaultdict

with open('day10_input.txt') as f:
    adapters = (sorted([0] + [int(line) for line in f]))

# Part one
DEVICE_BUILT_IN_ADAPTER = 3
adapters.append(max(adapters) + DEVICE_BUILT_IN_ADAPTER)
differences = defaultdict(int)
outlet = 0
for joltage in adapters:
    differences[joltage - outlet] += 1
    outlet = joltage
print(differences[1] * differences[3])

# Part two
number_of_paths = defaultdict(int)
number_of_paths[0] = 1
for joltage in adapters[1:]: # Must skip re-assigning 0 joltage outlet.
    number_of_paths[joltage] = number_of_paths[joltage-3] + number_of_paths[joltage-2] + number_of_paths[joltage-1]
print(number_of_paths[adapters[-1]])
