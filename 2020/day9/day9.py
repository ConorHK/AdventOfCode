#!/usr/bin/env python3

numbers = []
with open('day9_input.txt') as f:
    for line in f:
        numbers.append(int(line))

# Part 1
start_pos = 0
end_pos = 25
invalid_number = 0
prev_25 = numbers[start_pos:end_pos]
for number in numbers[end_pos:]:
    found = False
    for i in range(0, len(prev_25)):
       match = number - prev_25[i]
       if match in prev_25:
           found = True
           continue
    if found == False:
        invalid_number = number
    start_pos += 1
    end_pos += 1
    prev_25 = numbers[start_pos: end_pos]

print(invalid_number)

# Part 2
output = None
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        curr_sum = numbers[i:j]
        if sum(curr_sum) == invalid_number:
            output =(min(curr_sum) + max(curr_sum))
            break
        if sum(curr_sum) > invalid_number:
            break
    if output is not None:
        break
print(output)
