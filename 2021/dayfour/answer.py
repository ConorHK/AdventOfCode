import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

numbers = [int(number) for number in lines[0].strip().split(",")]

matrix = []
matrices = []
for line in lines[2:]:
    if len(line.strip()) != 0:
        elements = [
            int(element) for element in line.strip().split(" ") if not element == ""
        ]
        matrix.append(elements)
    else:
        matrices.append(np.array(matrix))
        matrix = []


def get_winning_matrix(matrices):
    for position, number in enumerate(numbers):
        for matrix_num, matrix in enumerate(matrices):
            if (-5 in matrix.sum(axis=0)) or (-5 in matrix.sum(axis=1)):
                return matrix_num, position
            matrices[matrix_num] = np.where(matrix == number, -1, matrix)


def get_answer():
    winning_matrix_num, last_number = get_winning_matrix(matrices)
    winning_matrix = matrices[winning_matrix_num]
    removed_negatives = (winning_matrix > -1) * winning_matrix
    return removed_negatives.sum() * numbers[last_number - 1]


# part one
print(get_answer())

# part two
while len(matrices) > 1:
    winning_matrix_num, last_number = get_winning_matrix(matrices)
    matrices.pop(winning_matrix_num)

print(get_answer())
