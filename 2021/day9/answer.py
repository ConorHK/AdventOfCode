from collections import defaultdict
from collections import Counter
from math import prod

matrix = []
with open("input.txt") as f:
    for line in f.readlines():
        matrix.append([int(number) for number in line.strip()])


basin_size = defaultdict(lambda: 0)


def find_basin_size(x, y):
    basin = matrix[x][y]
    if basin == 9:
        return x, y, -1
    column_length = len(matrix[x]) - 1
    row_length = len(matrix) - 1
    while True:
        up = matrix[max(x - 1, 0)][y]
        down = matrix[min(x + 1, row_length)][y]
        left = matrix[x][max(y - 1, 0)]
        right = matrix[x][min(y + 1, column_length)]

        if up == down == left == right == basin:
            return x, y, -1
        elif up < basin:
            basin = up
            x = x - 1
        elif down < basin:
            basin = down
            x = x + 1
        elif left < basin:
            basin = left
            y = y - 1
        elif right < basin:
            basin = right
            y = y + 1
        else:
            basin_size[str((x, y, basin))] += 1
            return x, y, basin


basins = set()
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        basins.add(find_basin_size(x, y))

print(sum([value[2] + 1 for value in basins]))
print(prod([value for _, value in Counter(basin_size).most_common(3)]))
