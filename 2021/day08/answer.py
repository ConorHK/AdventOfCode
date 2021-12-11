from collections import Counter


zero = {"a", "b", "c", "e", "f", "g"}
one = {"c", "f"}
two = {"a", "c", "d", "e", "g"}
three = {"a", "c", "d", "f", "g"}
four = {"b", "c", "d", "f"}
five = {"a", "b", "d", "f", "g"}
six = {"a", "b", "d", "e", "f", "g"}
seven = {"a", "c", "f"}
eight = {"a", "b", "c", "d", "e", "f", "g"}
nine = {"a", "b", "c", "d", "f", "g"}
NUMBER_MAP = {
    0: zero,
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
}

outputs = []
with open("input.txt") as f:
    for line in f.readlines():
        lines = line.split("|")
        outputs.append((lines[0].split(" "), lines[1].strip().split(" ")))


# part one
total = 0
for _, output_digits in outputs:
    count = Counter([len(digits) for digits in output_digits])
    total += sum(
        [
            count[len(one)],
            count[len(four)],
            count[len(seven)],
            count[len(eight)],
        ]
    )
print(total)

# part two
COMMON_DIGITS = {}
for number, value in NUMBER_MAP.items():
    COMMON_DIGITS[str([len(value & mask) for mask in [one, four, eight]])] = str(number)

total = 0
for numbers, output_digits in outputs:
    segment_lengths = {len(digit): set(digit) for digit in numbers}
    number = ""
    for output in map(set, output_digits):
        common = [
            len(output & segment_lengths[unique_matchings])
            for unique_matchings in [len(one), len(four), len(eight)]
        ]
        number += COMMON_DIGITS[str(common)]
    total += int(number)

print(total)
