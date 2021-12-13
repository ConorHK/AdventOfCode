from collections import Counter
import numpy as np

folds = []
points = []
with open("input.txt") as f:
    for line in f.readlines():
        if line.startswith("fold along"):
            _, _, split_info = line.strip().split(" ")
            axis, position = split_info.split("=")
            folds.append((axis, int(position)))
        elif not line.startswith("\n"):
            x, y = line.strip().split(",")
            points.append((int(x), int(y)))

points_copy = points.copy()


def fold(axis, position):
    global points
    if axis == "y":
        moving_points = list(filter(lambda x: x[1] > position, points))
        points = list(filter(lambda x: x[1] < position, points))
        for move in moving_points:
            movement = position - (move[1] - position)
            points.append((move[0], movement))
    elif axis == "x":
        moving_points = list(filter(lambda x: x[0] > position, points))
        points = list(filter(lambda x: x[0] < position, points))
        for move in moving_points:
            movement = position - (move[0] - position)
            points.append((movement, move[1]))


fold(*folds[0])
print(len(points) - len([k for k in Counter(points).values() if k > 1]))

points = points_copy
for fold_instructions in folds:
    fold(*fold_instructions)

array = np.zeros((6, 40), bool)
for x, y in points:
    array[y, x] = 1
print(np.array2string(array, separator="", formatter={"bool": {0: " ", 1: "X"}.get}))
