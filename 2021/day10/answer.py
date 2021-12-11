# messy, hasnt been cleaned up
from statistics import median
from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()

opening_tags = ["(", "{", "[", "<"]
closing_tags = [")", "}", "]", ">"]
corrupt_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
incomplete_points = {")": 1, "]": 2, "}": 3, ">": 4}
tag_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
}
result = {")": [], "]": [], "}": [], ">": []}
points = []
for line in lines:
    tagcount = defaultdict(lambda: [])
    depth = 0
    point = 0
    line_corrupt = False
    for tag in line.strip():
        if tag in opening_tags:
            depth += 1
            tagcount[depth].append(tag)
        if tag in closing_tags:
            if tag_map[tag] not in tagcount[depth]:
                result[tag].append(corrupt_points[tag])
                line_corrupt = True
                break

            tagcount[depth].remove(tag_map[tag])
            depth -= 1
    if not line_corrupt:
        populated_tagcount = {key: value for key, value in tagcount.items() if value}
        completion_order = sorted(populated_tagcount, reverse=True)
        opening_tagcount = {
            key: value
            for key, value in populated_tagcount.items()
            if key in opening_tags
        }
        for tag_position in range(completion_order[0], completion_order[-1] - 1, -1):
            tag = populated_tagcount[tag_position][0]
            point = (5 * point) + incomplete_points[tag_map[tag]]
        points.append(point)

# part one
total = 0
for key, value in result.items():
    total += value[0] * len(value)
print(total)
# part two
print(median(points))
