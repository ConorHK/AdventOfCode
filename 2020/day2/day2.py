#!/usr/bin/env python3

import re
with open('day2_input.txt') as f:
    pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    passwords = [pattern.match(x).groups() for x in f.readlines()]

correct_passwords = [int(lower_limit) <= password.count(letter) <= int(upper_limit) for (lower_limit, upper_limit, letter, password) in passwords]

print(sum(correct_passwords))

correct_passwords = [(letter == password[int(first_position)-1]) != (letter == password[int(second_position)-1]) for (first_position, second_position, letter, password) in passwords]

print(sum(correct_passwords))
