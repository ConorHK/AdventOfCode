from collections import defaultdict

START = "start"
END = "end"


class Vertex:
    def __init__(self, name) -> None:
        self.name = name
        self.neighbours = []
        self.is_start = self.name == START
        self.is_end = self.name == END

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


vertices = {}
with open("sample.txt") as f:
    for line in f.readlines():
        vertex_one, vertex_two = map(Vertex, line.strip().split("-"))
        if str(vertex_one) in vertices:
            vertices[str(vertex_one)].add_neighbour(vertex_two)
        else:
            vertex_one.add_neighbour(vertex_two)
            vertices[str(vertex_one)] = vertex_one

        if str(vertex_two) in vertices:
            vertices[str(vertex_two)].add_neighbour(vertex_one)
        else:
            vertex_two.add_neighbour(vertex_one)
            vertices[str(vertex_two)] = vertex_two

edges = defaultdict(list)
with open("sample.txt") as f:
    for line in f.readlines():
        vertex_one, vertex_two = line.strip().split("-")
        edges[vertex_one].append(vertex_two)
        edges[vertex_two].append(vertex_one)


def total_paths(vertex=vertices[START], seen=set(), seen_two_small_caves=False):
    print(vertex)
    if vertex.is_end:
        return 1
    if vertex in seen:
        if vertex.is_start:
            return 0
        if str(vertex).islower():
            if seen_two_small_caves:
                return 0
            seen_two_small_caves = True
    return sum(
        total_paths(neighbour, seen | {vertex}, seen_two_small_caves)
        for neighbour in vertex.neighbours
    )


print(total_paths(seen_two_small_caves=True))
print(total_paths())
