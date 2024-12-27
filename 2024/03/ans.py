from __future__ import annotations
"""
The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!
It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.
However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
For example, consider the following section of corrupted memory:
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

---
Assumptions:
* Sounds like an abstract syntax tree parser that drops malformed functions
* Naive solution: regex to match numbers in valid format
* Proper: AST parser

---
Approach:
* re match group of numbers inside mul( , ) where number can be 1-3 digits long

func get_numbers(instruction):
    number_tuples = re.match("regular expression following constraints")
    return number tuples
result = 0
for number_one, number_two in get_numbers(instruction):
    result  += number_one * number_two

"""
import re
from pathlib import Path


EXPRESSION = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def get_instruction() -> str:
    instruction = ""
    with Path("input.txt").open("r") as input_instruction:
        for line in input_instruction.readlines():
            instruction += line
    instruction.strip()
    return instruction


def get_numbers(instruction: str, expression=EXPRESSION) -> list[tuple[int, int]]:
    numbers = [(int(first), int(second)) for first, second in re.findall(expression, instruction)]
    print(numbers)
    return numbers


def get_result(numbers: list[tuple[int,int]]) -> int:
    return sum(first * second for first, second in numbers)


print(get_result(numbers=get_numbers(get_instruction())))

"""
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?

---
Approach:
* Same as before, but filter for matches with do() in front, then grab everything except for don't()
* Does the program start in do or don't? seems starts in do. Need to split on everything before first don't.

---
Changed approach to just split on don'ts and do's and then re-use regular expression
"""

def get_enabled_sections(instruction):
    numbers = []
    enabled = instruction.split("do()")
    if not len(enabled) > 1:
        return []
    for inst in enabled[1:]:
        numbers.extend(get_numbers(inst))
    return numbers


instruction = get_instruction().split("don't()")

output = get_result(numbers=get_numbers(instruction=instruction[0]))
for instruction_split in instruction:
    output += get_result(get_enabled_sections(instruction_split))
print(output)
