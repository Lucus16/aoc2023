import sys


def get_needed(results):
    bag = dict()
    for result in results.split(";"):
        for color_result in result.split(","):
            count, color = color_result.split()
            bag[color] = max(int(count), bag.get(color, 0))
    return bag


def is_valid(hand, bag):
    return all(hand[color] <= bag[color] for color in bag)


def product(it):
    total = 1
    for x in it:
        total *= x
    return total


lines = sys.stdin.read().splitlines()
games = (line.split(":") for line in lines)
games = {int(game_id.split()[1]): get_needed(results) for game_id, results in games}
bag = {"red": 12, "green": 13, "blue": 14}

print(sum(game_id for game_id, results in games.items() if is_valid(results, bag)))
print(sum(product(hand[color] for color in bag) for hand in games.values()))
