from collections import defaultdict

with open("input.txt") as f:
    positions = [int(number) for number in f.read().strip().split(",")]


def get_fuel_usage(increment):
    fuel = 88888888888888
    for crab_position in range(max(positions) + 1):
        moves = defaultdict(lambda: 0)
        for index, value in enumerate(positions):
            moves[index] += increment(abs(value - crab_position))
        move_sum = sum(moves.values())
        if move_sum < fuel:
            fuel = move_sum
    return fuel


print(f"part one: {get_fuel_usage(increment=lambda x: x)}")
print(f"part_two: {get_fuel_usage(increment=lambda x: sum(range(x + 1)))}")
