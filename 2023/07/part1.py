from collections import Counter
cards = "23456789TJQKA"
def score_hand(h):
    return [tuple(reversed(sorted((Counter(h[0]).values()))))] + [cards.index(c) for c in h[0]] 
hands = [line.split() for line in open("input.txt").readlines()]
hands.sort(key=score_hand)
print(sum([(i+1) * int(h[1]) for i, h in enumerate(hands)]))