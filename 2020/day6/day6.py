#!/usr/bin/env python3
# from string import ascii_lowercase

inp = open('day6_input.txt').read().strip().split('\n\n')
print(sum(len(set.union(*map(set, x.split('\n')))) for x in inp))
print(sum(len(set.intersection(*map(set, x.split('\n')))) for x in inp))

# part_one_total = 0
# for group in groups:
#     customs = set()
#     group = group.replace("\n", "")
#     for yes in group:
#        customs.add(yes)
#     part_one_total += len(customs)

# part_two_total = 0
# for group in groups:
#     group_length = 1
#     group_dict = {}
#     for yes in group:
#         if yes == '\n':
#             group_length += 1
#             continue
#         if yes not in group_dict:
#             group_dict[yes] = 1
#         else:
#             group_dict[yes] += 1
#     print(group_dict)
#     for custom, number_of_yes in group_dict.items():
#         if number_of_yes == group_length:
#             part_two_total += 1
