import sys


def get_area(instructions):
    x = 0
    edge_size = 0
    walls = []
    for direction, distance in instructions:
        distance = int(distance)
        edge_size += distance
        if direction == "R":
            x += distance
        if direction == "L":
            x -= distance
        if direction == "D":
            walls.append((x, distance))
        if direction == "U":
            walls.append((x, -distance))

    area = 0
    wallit = iter(sorted(walls))
    prev_x, l = next(wallit)
    for x, dl in wallit:
        area += (x - prev_x) * l
        prev_x = x
        l += dl
    # account for edges and corners
    return abs(area) + edge_size // 2 + 1


instructions = [line.split() for line in sys.stdin.read().splitlines()]
print(get_area((d, dist) for d, dist, color in instructions))


def decode_color(color):
    distance = int(color[2:-2], 16)
    direction = "RDLU"[int(color[-2])]
    return direction, distance


print(get_area(decode_color(color) for d, dist, color in instructions))
