#!/usr/bin/env python3

import math, collections, re

lines = open('day7_input.txt').read().strip().split('\n')

contained_in = collections.defaultdict(set)
contains = collections.defaultdict(list)
for line in lines:
    color = re.match(r'(.+?) bags contain', line)[1]
    for ct, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        ct = int(ct)
        contained_in[innercolor].add(color)
        contains[color].append((ct, innercolor))

holdscolor = set()
def check(color):
    for c in contained_in[color]:
        holdscolor.add(c)
        check(c)
check('shiny gold')
print(len(holdscolor))

def holds(color):
    total = 0
    for ct, inner in contains[color]:
        total += ct
        total += ct * holds(inner)
    return total
print(holds('shiny gold'))
