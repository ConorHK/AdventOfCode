with open("input.txt") as f:
    fish = [int(number) for number in f.read().strip().split(",")]

days = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for value in fish:
    days[value] += 1

for tick in range(256):
    if tick == 80:
        print(sum(days))
    if days[0] >= 1:
        days[9] += days[0]
        days[7] += days[0]
        days[0] -= days[0]
    days = days[1:] + days[:1]

print(sum(days))
