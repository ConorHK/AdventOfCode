from re import findall


with open("input.txt") as f:
    x_min, x_max, y_min, y_max = map(int, findall(r"\d+", f.read()))


def shoot(x_velocity, y_velocity):
    x_position = 0
    y_position = 0

    while y_position < y_min:
        x_position += x_velocity
        y_position -= y_velocity

        if x_velocity > 0:
            x_velocity -= 1

        y_velocity -= 1
        if x_min <= x_position <= x_max and y_min >= y_position >= y_max:
            return 1

    return 0


velocities = [(x, y) for x in range(1, x_max + 1) for y in range(-y_min, y_min)]
print(sum(i for i in range(abs(y_min))))
print(sum(shoot(*velocity) for velocity in velocities))
