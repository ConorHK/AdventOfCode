#!/usr/bin/env python3

translation = str.maketrans('FBLR', '0101')
seats = {int(bording_pass.translate(translation), 2) for bording_pass in open('day5_input.txt')}

print(max(seats), max({*range(max(seats))} - seats))
