"""
As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
..X...
.SAMX.
.A..A.
XMAS.S
.X....
Take a look at the little Elf's word search. How many times does XMAS appear?

....;1111.
.$$$$;2...
...&..2...
..&.^.2S.5
4443332.75
&.....^7.5
S.S.9.7.!5
.%.9.8.!.6
..9.8.!.*6
.9.8.!@@@6

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
---
Approach:
Search for all X's
From there Breadth first search in all 8 directions. Count up number of xmas strings (as could be more than one).
Mark X as visited.
Continue
"""
from itertools import product
from collections import deque
from pathlib import Path

SAMPLE = [
    ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M", ],
    ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A", ],
    ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M", ],
    ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X", ],
    ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M", ],
    ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A", ],
    ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S", ],
    ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A", ],
    ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M", ],
    ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X", ],
]


def get_word_search():
    output = []
    with Path("input.txt").open("r") as word_search: 
        for line in word_search.readlines():
            output.append(list(line.strip()))
    return output


def positions_of_x(word_search, bounds):
    rows, columns = bounds
    x_positions = []
    for x_pos, y_pos in product(range(rows), range(columns)):
        if word_search[x_pos][y_pos] == "X":
            x_positions.append((x_pos, y_pos))
    return x_positions


def is_in_bounds(bounds, position):
    x, y = position
    width, height = bounds
    return 0 <= x < width and 0 <= y < height


def get_x_neighbours(position, bounds, word_search):
    x, y = position
    output = set()
    neighbour_map = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for dx, dy in neighbour_map:
        row, column = x + dx, y + dy
        if is_in_bounds(bounds, (row, column)):
            output.add((row, column, (dx, dy)))
    return output


def search_neighbors_for_xmas(position, bounds, word_search, remaining_word):
    x, y, direction = position
    if word_search[x][y] != remaining_word.popleft():
        return
    if len(remaining_word) <= 0:
        return position

    next_position = (x + direction[0], y + direction[1])
    if not is_in_bounds(bounds=bounds, position=next_position):
        return
    next_position = (next_position[0], next_position[1], direction)
    return search_neighbors_for_xmas(
        position=next_position,
        bounds=bounds,
        word_search=word_search,
        remaining_word=remaining_word
    )


word_search = get_word_search()
bounds = len(word_search), len(word_search[0])
start_positions = positions_of_x(word_search=word_search, bounds=bounds)
result = []
for position in start_positions:
    neighbours = get_x_neighbours(position, bounds, word_search)
    for neighbour in neighbours:
        result.append(search_neighbors_for_xmas(position=neighbour, bounds=bounds, word_search=word_search, remaining_word=deque(["M", "A", "S"].copy())))
print(len([x for x in result if x]))


"""
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

--- 
Approach:
* Find all A's 
* Search the diagonal neighbours
* If as expected, increment result

"""

def get_a_cross_point(position, bounds, word_search):
    x, y = position
    output = set()
    neighbour_map = [(-1, -1), (-1, 1)]
    for dx, dy in neighbour_map:
        row, column = x + dx, y + dy
        if is_in_bounds(bounds, (row, column)):
            output.add((row, column, (dx, dy)))
    return output

def positions_of_a(word_search, bounds):
    rows, columns = bounds
    x_positions = []
    for x_pos, y_pos in product(range(rows), range(columns)):
        if word_search[x_pos][y_pos] == "A":
            x_positions.append((x_pos, y_pos))
    return x_positions


LETTER_MAP = {
    "M": "S",
    "S": "M",
}


def search_neighbors_for_mas_cross(position, bounds, word_search, letters):
    x, y, direction = position
    letter = word_search[x][y]
    if letter not in letters:
        return False
    letters.remove(letter)
    if len(letters) == 0:
        return True

    """
    if we have -1, -1, x is 0, y is 0
    we need to go to 2, 2, -> therefore add 2 to each

    if we have -1, 1 x is 0, y is 2
    we need to go to 2, 0 -> therefore add 2, minus 2
    """
    if direction == (-1, -1):
        next_position = (x + 2, y + 2)
    else:
        next_position = (x + 2, y - 2)
    if not is_in_bounds(bounds=bounds, position=next_position):
        return False

    next_position = (next_position[0], next_position[1], direction)
    return search_neighbors_for_mas_cross(
        position=next_position,
        bounds=bounds,
        word_search=word_search,
        letters=letters
    )

word_search = get_word_search()
bounds = len(word_search), len(word_search[0])
start_positions = positions_of_a(word_search=word_search, bounds=bounds)
result = []
for position in start_positions:
    neighbours = get_a_cross_point(position, bounds, word_search)
    if neighbours:
        res = all(search_neighbors_for_mas_cross(position=neighbour, bounds=bounds, word_search=word_search, letters=["M", "S"].copy()) for neighbour in neighbours)
        if res:
            result.append(position)
print(len([x for x in result if x]))
