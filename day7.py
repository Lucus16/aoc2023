import sys


def hand_type(hand):
    return list(reversed(sorted(hand.count(card) for card in hand)))


def hand_key(hand):
    return (hand_type(hand), ["23456789TJQKA".index(card) for card in hand])


lines = [line.split() for line in sys.stdin.read().splitlines()]
hand_bids = [(hand, int(bid)) for hand, bid in lines]
hand_bids.sort(key=lambda x: hand_key(x[0]))
print(sum((1 + rank) * x[1] for rank, x in enumerate(hand_bids)))


def joker_hand_key(hand):
    counts = {card: hand.count(card) for card in hand}
    joker_count = counts.get("J", 0)
    counts["J"] = 0
    most_common = max(hand, key=lambda card: counts[card])
    typ = hand_type([most_common if card == "J" else card for card in hand])
    return (typ, ["J23456789TQKA".index(card) for card in hand])


hand_bids.sort(key=lambda x: joker_hand_key(x[0]))
print(sum((1 + rank) * x[1] for rank, x in enumerate(hand_bids)))
