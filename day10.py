import sys

pipes = [[c for c in line] for line in sys.stdin.read().splitlines()]

bends = {
    "vL": ">",
    "<L": "^",
    ">J": "^",
    "vJ": "<",
    "^7": "<",
    ">7": "v",
    "<F": "v",
    "^F": ">",
    "v|": "v",
    "^|": "^",
    ">-": ">",
    "<-": "<",
}

deltas = {
    "v": (0, 1),
    ">": (1, 0),
    "^": (0, -1),
    "<": (-1, 0),
}

start = next(
    (x, y) for y, line in enumerate(pipes) for x, c in enumerate(line) if c == "S"
)

for direction, delta in deltas.items():
    x, y = start[0] + delta[0], start[1] + delta[1]
    key = direction + pipes[y][x]
    if key in bends:
        break

edge_size = 1
walls = []
while (x, y) != start:
    direction = bends[direction + pipes[y][x]]
    edge_size += 1
    x += deltas[direction][0]
    y += deltas[direction][1]
    if direction == "<":
        walls.append((y, 1))
    elif direction == ">":
        walls.append((y, -1))

print(edge_size // 2)

area = 0
wallit = iter(sorted(walls))
prev_x, l = next(wallit)
for x, dl in wallit:
    area += (x - prev_x) * l
    prev_x = x
    l += dl

print(abs(area) + 1 - edge_size // 2)
