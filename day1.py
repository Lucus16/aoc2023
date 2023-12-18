import sys
import re

digit_numbers = {str(d): d for d in range(1, 10)}
digit_names = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def calibrate(line, allowed_digits):
    # find *overlapping* matches by not consuming the match
    ds = re.findall("(?=(" + "|".join(allowed_digits) + "))", line)
    return 10 * allowed_digits[ds[0]] + allowed_digits[ds[-1]]


lines = sys.stdin.read().splitlines()
print(sum(calibrate(line, digit_numbers) for line in lines))
print(sum(calibrate(line, digit_numbers | digit_names) for line in lines))
