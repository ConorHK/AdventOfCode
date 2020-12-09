#!/usr/bin/env python3
import re
passports = open('day4_input.txt').read().strip().split('\n\n')

fields = {
    'byr': lambda x: 2002 >= int(x) >= 1920,
    'iyr': lambda x: 2020 >= int(x) >= 2010,
    'eyr': lambda x: 2030 >= int(x) >= 2020,
    'hgt': lambda x: (x.endswith('cm') and 193 >= int(x[:-2]) >= 150) or (x.endswith('in') and 76 >= int(x[:-2]) >= 59),
    'hcl': lambda x: re.match('^#[a-f\d]{6}$', x) != None,
    'ecl': lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda x: len(x) == 9  and x.isdigit(),
}

part_one = part_two = 0
for passport in passports:
    parts = re.split('\s', passport)
    passport_dict = dict(part.split(':') for part in parts)
    if all(key in passport_dict for key in fields):
        part_one += 1
        if all(fields[key](passport_dict[key]) for key in fields):
            part_two += 1
print(part_one, part_two)

