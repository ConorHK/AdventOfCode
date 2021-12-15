from contextlib import suppress
from collections import defaultdict

PART_ONE = 10
PART_TWO = 40

with open("input.txt") as f:
    lines = f.readlines()
    polymer = lines[0].strip()
    instructions = {}
    for instruction in lines[2:]:
        pattern, insertion = instruction.strip().split(" -> ")
        instructions[pattern] = insertion


def grow(iterations):
    pair_count = defaultdict(lambda: 0)
    characters = defaultdict(lambda: 0)

    for number, character in enumerate(polymer):
        with suppress(IndexError):
            characters[character] += 1
            pair = character + polymer[number + 1]
            pair_count[pair] += 1

    for _ in range(iterations):
        pair_items = pair_count.copy().items()

        for (element_one, element_two), count in pair_items:
            insertion = instructions[element_one + element_two]
            characters[insertion] += count

            pair_count[element_one + insertion] += count
            pair_count[insertion + element_two] += count

            pair_count[element_one + element_two] -= count

    return (max(characters.values()) - min(characters.values()))


print(grow(PART_ONE))
print(grow(PART_TWO))
