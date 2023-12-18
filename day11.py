import sys

stars = sys.stdin.read().splitlines()
total_stars = sum(c == "#" for line in stars for c in line)


def vertical_sum(stars, empty_factor):
    total = 0
    passed = 0
    for line in stars:
        line_stars = sum(c == "#" for c in line)
        passed += line_stars
        if line_stars == 0:
            total += passed * (total_stars - passed) * empty_factor
        else:
            total += passed * (total_stars - passed)
    return total


print(vertical_sum(stars, 2) + vertical_sum(zip(*stars), 2))
print(vertical_sum(stars, 1000000) + vertical_sum(zip(*stars), 1000000))
