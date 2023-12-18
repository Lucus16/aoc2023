import sys


def score_card(winning, have):
    return len(set(winning.split()) & set(have.split()))


lines = sys.stdin.read().splitlines()
cards = [score_card(*line.split(":")[1].split("|")) for line in lines]

print(sum(((1 << score) >> 1) for score in cards))

card_count = [1 for card in cards]
for i, score in enumerate(cards):
    for j in range(i + 1, i + 1 + score):
        card_count[j] += card_count[i]

print(sum(card_count))
