from collections import defaultdict

with open("input.txt") as f:
    positions = [int(number) for number in f.read().strip().split(",")]

def get_fuel_usage(increment):
    fuel_costs = []
    for crab_position in range(max(positions) + 1):
        moves = defaultdict(lambda: 0)
        for index, value in enumerate(positions):
            moves[index] += increment(abs(value - crab_position))
        fuel_costs.append(sum(moves.values()))
    return min(fuel_costs)


print(f"part one: {get_fuel_usage(increment=lambda x: x)}")
print(f"part_two: {get_fuel_usage(increment=lambda x: sum(range(x + 1)))}")
