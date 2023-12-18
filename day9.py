import sys


def extrapolate(xs):
    if all(x == 0 for x in xs):
        return 0
    else:
        return xs[-1] + extrapolate([x2 - x1 for x1, x2 in zip(xs[:-1], xs[1:])])


lines = [[int(x) for x in line.split()] for line in sys.stdin.read().splitlines()]

print(sum(extrapolate(series) for series in lines))
print(sum(extrapolate(list(reversed(series))) for series in lines))
