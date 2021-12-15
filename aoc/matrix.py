from typing import Tuple, Union, Any, Set
import numpy as np


def numpy_from_file(filename: str, var_type: type = int) -> np.ndarray:
    """
    Creates numpy array from a nondelimited text file.

    :param filename: filename string
    :param var_type: optional typing of variable, defaults to integer
    :returns: Numpy array
    """
    return np.genfromtxt(filename, dtype=var_type, delimiter=1)


def neighbours(
    position: Tuple[int, int],
    array_size: Union[Tuple[int, int], Any],
    diagonal: bool = False,
) -> Set[Tuple[int, int]]:
    """
    Returns list of surrounding positions for a position in a 2D array.

    :param position: x, y tuple
    :param array_size: width, height tuple
    :param diagonal: optional, includes diagonal neighbours
    :returns: List of surrounding positions
    """
    x, y = position
    width, height = array_size
    output = set()
    neighbour_map = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    if diagonal:
        neighbour_map.extend([(-1, -1), (1, -1), (-1, 1), (1, 1)])
    for dx, dy in neighbour_map:
        row, column = x + dx, y + dy
        if 0 <= row < width and 0 <= column < height:
            output.add((row, column))
    return output
