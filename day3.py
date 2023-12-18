import sys
import re


def issymbol(c):
    return c != "." and not c.isdecimal()


lines = sys.stdin.read().splitlines()
numberlines = [["." if issymbol(c) else c for c in line] for line in lines]
close1 = [-1, 0, 1]
close2 = [(x, y) for x in close1 for y in close1]


def product(it):
    total = 1
    for x in it:
        total *= x
    return total


def find_partnums(lines):
    width = len(lines[0])
    height = len(lines)
    for y, line in enumerate(lines):
        for m in re.finditer("\d+", line):
            x1 = m.start()
            x2 = x1 + len(m.group())
            value = int(m.group())
            is_partnum = any(
                issymbol(lines[y_][x_])
                for y_ in range(max(0, y - 1), min(height, y + 2))
                for x_ in range(max(0, x1 - 1), min(width, x2 + 1))
            )
            if is_partnum:
                yield value


print(sum(find_partnums(lines)))


def get_partnums_near(lines, x, y):
    numberlines[y][x] = "*"
    result = find_partnums(["".join(line) for line in numberlines[y - 1 : y + 2]])
    numberlines[y][x] = "."
    return result


def find_gear_ratios(lines):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "*":
                partnums = list(get_partnums_near(lines, x, y))
                if len(partnums) == 2:
                    yield product(partnums)


print(sum(find_gear_ratios(lines)))
