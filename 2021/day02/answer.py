# part one
instructions = {"forward": 0, "down": 0, "up": 0}
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        instructions[line[0]] += int(line[1])
depth = instructions["down"] - instructions["up"]
print(instructions["forward"] * depth)

# part two
forward = 0
aim = 0
depth = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        unit = int(line[1])
        if line[0] == "forward":
            forward += unit
            depth += unit * aim
        if line[0] == "down":
            aim += unit
        if line[0] == "up":
            aim -= unit
print(forward * depth)
