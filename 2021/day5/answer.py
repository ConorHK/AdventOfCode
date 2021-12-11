import re
import numpy as np


class Line:
    def __init__(self, coordinates) -> None:
        self.x1 = coordinates[0]
        self.y1 = coordinates[1]
        self.x2 = coordinates[2]
        self.y2 = coordinates[3]

    def vertical(self):
        return self.y1 == self.y2

    def horizontal(self):
        return self.x1 == self.x2

    def x_order(self):
        start = self.x1 if self.x1 < self.x2 else self.x2
        end = self.x2 if self.x1 < self.x2 else self.x1
        return start, end

    def y_order(self):
        start = self.y1 if self.y1 < self.y2 else self.y2
        end = self.y2 if self.y1 < self.y2 else self.y1
        return start, end

    def position(self):
        if self.horizontal():
            start, end = self.y_order()
            return self.x1, list(range(start, end + 1))
        elif self.vertical():
            start, end = self.x_order()
            return list(range(start, end + 1)), self.y1
        else:
            if self.x1 > self.x2:
                start_x, start_y, end_x, end_y = self.x2, self.y2, self.x1, self.y1
            else:
                start_x, start_y, end_x, end_y = self.x1, self.y1, self.x2, self.y2

            x_pos = []
            y_pos = []
            slope = (end_y - start_y) // (end_x - start_x)
            for x, y in zip(range(start_x, end_x), range(start_y, end_y, slope)):
                x_pos.append(x)
                y_pos.append(y)
            x_pos.append(end_x)
            y_pos.append(end_y)
            return x_pos, y_pos


with open("input.txt") as f:
    lines = f.readlines()

max_x = 0
max_y = 0
segments = []
for line in lines:
    coordinates = [int(num) for num in re.findall(r"\d+", line)]
    local_max_x = max(coordinates[0], coordinates[2])
    local_max_y = max(coordinates[1], coordinates[3])
    max_x = local_max_x if local_max_x > max_x else max_x
    max_y = local_max_y if local_max_y > max_y else max_y
    segments.append(Line(coordinates=coordinates))

map = np.zeros((max_x + 2, max_y + 2))
for line in segments:
    if line.horizontal():
        x, y = line.position()
        for number in range(len(y)):
            map[y[number], x] += 1
    elif line.vertical():
        x, y = line.position()
        for number in range(len(x)):
            map[y, x[number]] += 1
    else:  # part two, comment out for part one
        x, y = line.position()
        for x_pos, y_pos in zip(x, y):
            map[y_pos, x_pos] += 1

print((map > 1).sum())
