from collections import Counter
cards = "J23456789TQKA"
def score_hand(h, orig):
    return [tuple(reversed(sorted((Counter(h[0]).values()))))] + [cards.index(c) for c in orig] 
def score_hand_best(h):
    return max([score_hand([h[0].replace("J", cards[i])], h[0]) for i in range(len(cards))])
hands = [line.split() for line in open("input.txt").readlines()]
hands.sort(key=score_hand_best)
print(sum([(i+1) * int(h[1]) for i, h in enumerate(hands)]))