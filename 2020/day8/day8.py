#!/usr/bin/env python3

stack = [(command, int(number)) for command, number in map(str.split, open('day_8.txt'))]
ACC = 'acc'
NOP = 'nop'
JMP = 'jmp'
# Part 1
instruction_tracker = set()
accumulator = 0
instruction = 0
while True:
    if instruction in instruction_tracker:
        print(accumulator)
        break
    else:
        instruction_tracker.add(instruction)

    command, number = stack[instruction]
    instruction += number if command == JMP else 1
    accumulator += number if command == ACC else 0


# Part 2
def fixed_loop():
    accumulator = 0
    instruction = 0
    instruction_tracker = set()

    while instruction not in instruction_tracker and instruction < len(stack):
        command, number = stack[instruction]
        instruction += number if command == JMP else 1
        accumulator += number if command == ACC else 0
        instruction_tracker.add(instruction)

    return accumulator if instruction == len(stack) else None

swap = {JMP: NOP, NOP: JMP, ACC: ACC}
for instruction, (command, number), in enumerate(stack):
    stack[instruction] = swap[command], number

    output = fixed_loop()
    if output is not None:
        print(output)
        break
    stack[instruction] = command, number
