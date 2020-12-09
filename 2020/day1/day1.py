#!/usr/bin/env python3

SUM = 2020
expenses = []
with open('input.txt') as f:
    for line in f:
        expenses.append(int(line))

# Part 1
for i in range(0, len(expenses)):
    match = SUM - expenses[i]
    if match in expenses:
        print(str(expenses[i]) + " + " + str(match) + " = 2020")
        print(str(expenses[i]) + " * " + str(match) + " = " + str(expenses[i] * match))
        break

# Part 2
for i in range(0, len(expenses) - 2):
    s = set()
    match = SUM - expenses[i]
    for j in range(i + 1, len(expenses)):
            if (match - expenses[j]) in s:
                print(str(expenses[i]) + " + " + str(expenses[j]) + " + " + str(match - expenses[j]) + " = 2020")
                print(str(expenses[i]) + " * " + str(expenses[j]) + " * " + str(match - expenses[j]) + " = " + str(expenses[i] * expenses[j] * (match - expenses[j])))
                break
            s.add(expenses[j])
