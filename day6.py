import sys

lines = [line.split(":")[1] for line in sys.stdin.read().splitlines()]
times1, dists1 = [map(int, line.split()) for line in lines]
time2, dist2 = [int("".join(line.split())) for line in lines]


def product(it):
    total = 1
    for x in it:
        total *= x
    return total


def get_possible_wins(time, dist):
    scores = [(time - t) * t for t in range(0, time)]
    return sum(1 for score in scores if score > dist)


print(product(map(get_possible_wins, times1, dists1)))
print(get_possible_wins(time2, dist2))
