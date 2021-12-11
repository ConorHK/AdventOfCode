import numpy as np
from aoc.matrix import surrounding_positions, create_numpy_array_from_file

READY_TO_FLASH = 10
SIMULTANEOUS_FLASH = 0
FLASHED = 0

grid = create_numpy_array_from_file(filename="input.txt")


def flash(x, y):
    global flashes
    flashes += 1
    grid[x, y] = FLASHED
    for row in surrounding_positions(position=x, array_size=grid.shape[0]):
        for column in surrounding_positions(position=y, array_size=grid.shape[0]):
            if grid[row, column] != FLASHED:
                grid[row, column] += 1
                if grid[row, column] >= READY_TO_FLASH:
                    flash(x=row, y=column)


def run_simulation(iterations):
    global grid
    for iteration in range(iterations):
        if np.sum(grid) == SIMULTANEOUS_FLASH:
            return iteration
        grid = grid + 1
        for (x, y), octopus in np.ndenumerate(grid):
            if octopus >= READY_TO_FLASH:
                flash(x=x, y=y)
    return flashes


flashes = 0
grid_copy = grid.copy()
print(run_simulation(iterations=100))  # part one
grid = grid_copy
print(run_simulation(iterations=1000))  # part two
