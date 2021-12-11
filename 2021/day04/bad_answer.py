import itertools
import collections
with open("input.txt") as f:
    lines = f.readlines()

numbers = [int(number) for number in lines[0].strip().split(",")]
cards = {}
matrix = 0
rows = []
columns = {0: [], 1: [], 2: [], 3: [], 4: []}
card_numbers = collections.defaultdict(set)
for line in lines[2:]:
    if len(line.strip()) != 0:
        elements = [int(element) for element in line.strip().split(" ") if not element == ""]
        for column_number, element in enumerate(elements):
            columns[column_number].append(element)
            card_numbers[matrix].add(element)
        rows.append(elements)
    else:
        cards[matrix] = rows
        for _, value in columns.items():
            cards[matrix].append(value)
        matrix += 1
        column_number = 0
        rows = []
        columns = {0: [], 1: [], 2: [], 3: [], 4: []}
        bingo = []
        continue

chosen_numbers = []
winning_matrices = []
tuples = set()
for number in numbers:
    chosen_numbers.append(number)
    if len(chosen_numbers) >= 5:
        for answer in itertools.combinations(chosen_numbers, 5):
            tuples.add(answer)

    for matrix in range(len(cards)):
        for bingo in tuples:
            for win in cards[matrix]:
                if matrix not in winning_matrices:
                    group = [number for number in bingo if number in win]
                    if len(group) == 5:
                        if len(winning_matrices) == (len(cards) - 1):
                            winning_matrix = matrix
                            winning_group = group
                            break
                        winning_matrices.append( matrix)
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

total = 0
for number in card_numbers[winning_matrix]:
    if number not in chosen_numbers:
        total += number
        
print(total * chosen_numbers[-1])
