from typing import List
import numpy as np


def create_numpy_array_from_file(filename: str) -> np.ndarray:
    """
    Creates numpy array from a nondelimited text file.
    :param filename: filename string
    :returns: Numpy array
    """
    with open(filename) as f:
       return  np.array([[int(number) for number in line.strip()] for line in f.readlines()])

def surrounding_positions(position: int, array_size: int) -> List[int]:
    """
    Returns list of surrounding positions for an axis in a 2D array.
    e.g you want the row neighbors of 4 -> [3, 4, 5]
    Factors out positions outside the acceptible range.
    Intended for use with x, y calls etc. , hence including passed position.
    :param position: int position to find neighbours for
    :param array_size: size of array
    :returns: List of surrounding positions
    """
    return [
        position + neighbour
        for neighbour in range(-1, 2)
        if (0 <= position + neighbour < array_size)
    ]
