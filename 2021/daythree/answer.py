bitlist = []
with open("input.txt") as f:
    bitlist = [number.strip() for number in f.readlines()]


number_length = len(bitlist[0])
def get_common_bit(bitlist, position, most_common):
    half_bitlist_size = len(bitlist) / 2
    ones = 0
    if most_common:
        output_bit = "1"
        alternative_bit = "0"
    else:
        output_bit = "0"
        alternative_bit = "1"

    for number in bitlist:
        ones += int(number[position])
    if ones == 1 or ones == half_bitlist_size:
        return output_bit
    return output_bit if (ones > half_bitlist_size) else alternative_bit


# part one
gamma = ""
epsilon = ""
for position in range(number_length):
    gamma += get_common_bit(bitlist, position, most_common=True)
    epsilon += get_common_bit(bitlist, position, most_common=False)
print(int(gamma, 2) * int(epsilon, 2))

# part two
oxygenlist = bitlist.copy()
scrubberlist = bitlist.copy()
for position in range(number_length):
    most_common_bit = get_common_bit(oxygenlist, position, most_common=True)
    least_common_bit = get_common_bit(scrubberlist, position, most_common=False)
    oxygenlist = list(filter(lambda x: x[position] == most_common_bit, oxygenlist))
    scrubberlist = list(filter(lambda x: x[position] == least_common_bit, scrubberlist))
    if len(oxygenlist) == 1:
        oxygen = oxygenlist[0]
    if len(scrubberlist) == 1:
        scrubber = scrubberlist[0]

print(int(scrubber, 2) * int(oxygen, 2))
