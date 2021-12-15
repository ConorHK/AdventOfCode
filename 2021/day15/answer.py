from aoc.matrix import neighbours, numpy_from_file
from heapq import heappop, heappush
from numpy import concatenate

START = (0, 0)
GRID = numpy_from_file("input.txt")


def dijkstra(matrix):
    finish = tuple(k - 1 for k in matrix.shape)
    heap = [(0, START)]
    visited = set()
    while heap:
        total_risk, position = heappop(heap)
        if position == finish:
            return total_risk
        elif position not in visited:
            visited.add(position)
            for x, y in neighbours(position, matrix.shape):
                square_risk = (matrix[x, y] % 9) if matrix[x, y] > 9 else matrix[x, y]
                cost = square_risk + total_risk
                heappush(heap, (cost, (x, y)))


part_one = GRID.copy()
print(dijkstra(part_one))

part_two = GRID.copy()
for axis in [0, 1]:
    part_two = concatenate([part_two + i for i in range(5)], axis=axis)
print(dijkstra(part_two))
