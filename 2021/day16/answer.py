from math import prod
from collections import deque

LITERAL_VALUE = 4
BINARY = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

OPERATIONS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1],
}

with open("input.txt") as f:
    bytes = "".join(BINARY[hex_value] for hex_value in f.read().strip())
    bits = deque([bit for bit in bytes])


def number(bytes):
    return int("".join(bytes), 2)


def read_bits(size):
    output = []
    for _ in range(size):
        output.append(bits.popleft())
    return output


def literal():
    bytes_left = True
    packet = ""
    while bytes_left:
        if "1" in read_bits(1):
            packet += "".join(read_bits(4))
        else:
            bytes_left = False
            packet += "".join(read_bits(4))
    return int(packet, 2)


def operator(operation):
    length_type_id = int(read_bits(1)[0])
    values = []
    if length_type_id:
        total_subpackets = int("".join(read_bits(11)), 2)
        for _ in range(total_subpackets):
            values.append(parse_next_packet())
    else:
        total_length_of_subpackets = int("".join(read_bits(15)), 2)
        current_bit_length = len(bits)
        while len(bits) > current_bit_length - total_length_of_subpackets:
            values.append(parse_next_packet())

    return OPERATIONS[operation](values)


def parse_next_packet():
    global version_numbers
    version = number(read_bits(3))
    version_numbers += version
    type_id = number(read_bits(3))

    if type_id == LITERAL_VALUE:
        return literal()
    else:
        return operator(type_id)


version_numbers = 0
print(parse_next_packet())  # part two
print(version_numbers)  # part one
