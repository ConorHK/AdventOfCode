import numpy as np

FLASHED = -1
READY_TO_FLASH = 10
SIMULTANEOUS_FLASH = 0
START_ENERGY = 0

with open("input.txt") as f:
    grid = np.array(
        [[int(number) for number in line.strip()] for line in f.readlines()]
    )


def surrounding_rows(position):
    return [
        position + neighbor
        for neighbor in range(-1, 2)
        if (0 <= position + neighbor < grid.shape[0])
    ]


def flash(x, y):
    global flashes
    flashes += 1
    grid[x, y] = FLASHED
    for row in surrounding_rows(x):
        for column in surrounding_rows(y):
            if grid[row, column] != FLASHED:
                grid[row, column] += 1
                if grid[row, column] >= READY_TO_FLASH:
                    flash(x=row, y=column)


def run_simulation(iterations):
    global grid
    for iteration in range(iterations):
        grid = np.where(grid == FLASHED, START_ENERGY, grid)
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
