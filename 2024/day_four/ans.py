from __future__ import annotations
from itertools import product
from collections import deque
from pathlib import Path
from functools import cache

"""
Approach:
* Search for all X's
* From there search in all 8 directions. Count up number of xmas strings (as could be more than one).
* Continue
"""

SAMPLE = [
    [ "M", "M", "M", "S", "X", "X", "M", "A", "S", "M", ],
    [ "M", "S", "A", "M", "X", "M", "S", "M", "S", "A", ],
    [ "A", "M", "X", "S", "X", "M", "A", "A", "M", "M", ],
    [ "M", "S", "A", "M", "A", "S", "M", "S", "M", "X", ],
    [ "X", "M", "A", "S", "A", "M", "X", "A", "M", "M", ],
    [ "X", "X", "A", "M", "M", "X", "X", "A", "M", "A", ],
    [ "S", "M", "S", "M", "S", "A", "S", "X", "S", "S", ],
    [ "S", "A", "X", "A", "M", "A", "S", "A", "A", "A", ],
    [ "M", "A", "M", "M", "M", "X", "M", "M", "M", "M", ],
    [ "M", "X", "M", "X", "A", "X", "M", "A", "S", "X", ],
]


class Board:

    @classmethod
    def from_input(cls, input_path: Path) -> Board:
        output = []
        with input_path.open("r") as word_search:
            for line in word_search.readlines():
                output.append(list(line.strip()))
        return cls(content=output)

    def __init__(self, content: list[list[str]]) -> None:
        self.content = content

    @property
    @cache
    def width(self) -> int:
        return len(self.content)

    @property
    @cache
    def height(self) -> int:
        return len(self.content[0])

    @cache
    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def positions_of_letter(self, letter: str) -> set[tuple[int, int]]:
        positions = set()
        for x_pos, y_pos in product(range(self.width), range(self.height)):
            if self.content[x_pos][y_pos] == letter:
                positions.add((x_pos, y_pos))
        return positions

    def get_neighbours(
        self,
        position,
        neighbour_map: list[tuple[int, int]] = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, -1),
            (1, -1),
            (-1, 1),
            (1, 1),
        ],
    ) -> set[tuple[int, int]] | None:
        x, y = position
        output = set()
        for dx, dy in neighbour_map:
            row, column = x + dx, y + dy
            if self.is_in_bounds(x=row, y=column):
                output.add((row, column, (dx, dy)))
        return output if len(output) else None


def search_neighbors_for_xmas(position, word_search: Board, remaining_word):
    x, y, direction = position
    if word_search.content[x][y] != remaining_word.popleft():
        return 0
    if len(remaining_word) <= 0:
        return 1

    next_position = (x + direction[0], y + direction[1], direction)
    if not word_search.is_in_bounds(x=next_position[0], y=next_position[1]):
        return 0
    return search_neighbors_for_xmas(
        position=next_position, word_search=word_search, remaining_word=remaining_word
    )


word_search = Board(content=SAMPLE)
x_neighbours: list[set[tuple[int, int]]]= [
    x_neighbour
    for position in word_search.positions_of_letter(letter="X")
    if (x_neighbour:= word_search.get_neighbours(position))
]

print(
    sum(
        search_neighbors_for_xmas(
            position=neighbour,
            word_search=word_search,
            remaining_word=deque(["M", "A", "S"].copy()),
        )
        for neighbours in x_neighbours
        for neighbour in neighbours
    )
)


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
        if word_search.is_in_bounds(x=row, y=column):
            output.add((row, column, (dx, dy)))
    return output


def search_neighbors_for_mas_cross(position, word_search, letters):
    x, y, direction = position
    letter = word_search.content[x][y]
    if letter not in letters:
        return 0
    letters.remove(letter)
    if len(letters) == 0:
        return 1

    if direction == (-1, -1):
        next_position = (x + 2, y + 2)
    else:
        next_position = (x + 2, y - 2)

    if not word_search.is_in_bounds(x=next_position[0], y=next_position[1]):
        return 0

    next_position = (next_position[0], next_position[1], direction)
    return search_neighbors_for_mas_cross(
        position=next_position, word_search=word_search, letters=letters
    )


part_b_result = 0
a_cross_points = [
    neighbour
    for position in word_search.positions_of_letter(letter="A")
    for neighbour in [
        word_search.get_neighbours(position, neighbour_map=[(-1, -1), (-1, 1)])
    ]
    if neighbour is not None
]

for cross_point in a_cross_points:
    result = all(
        search_neighbors_for_mas_cross(
            position=neighbour,
            word_search=word_search,
            letters=["M", "S"].copy(),
        )
        for neighbour in cross_point
    )
    if result:
        part_b_result += 1
print(part_b_result)
