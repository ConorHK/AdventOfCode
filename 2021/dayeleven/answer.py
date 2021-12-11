import numpy as np

with open("input.txt") as f:
    grid = np.array(
        [[int(number) for number in line.strip()] for line in f.readlines()]
    )


flashes = 0


def surrounding_rows(position):
    return [
        position + neighbor
        for neighbor in range(-1, 2)
        if (0 <= position + neighbor < grid.shape[0])
    ]


def flash(x, y):
    global flashes
    flashes += 1
    grid[x, y] = -1
    for row in surrounding_rows(x):
        for column in surrounding_rows(y):
            if grid[row, column] != -1:
                grid[row, column] += 1
                if grid[row, column] >= 10:
                    flash(x=row, y=column)

def run_simulation(iterations):
    global grid
    for iteration in range(iterations):
        grid = np.where(grid == -1, 0, grid)
        if np.sum(grid) == 0:
            return iteration
        grid = grid + 1
        for (x, y), octopus in np.ndenumerate(grid):
            if octopus >= 10:
                flash(x=x, y=y)
    return flashes

grid_copy = grid.copy()
print(run_simulation(iterations=100))  # part one
grid = grid_copy
print(run_simulation(iterations=1000))  # part two
