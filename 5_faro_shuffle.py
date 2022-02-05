cards = input().split()
n_shuffles = int(input())
for n_shuffle in range(n_shuffles):
    top_card = cards[0]
    last_card = cards[-1]
    half = len(cards) // 2
    left_cards = []
    right_cards = []
    shuffle_cards = []
    for index in range(1, half):
        left_cards.append(cards[index])

    for index in range(half, len(cards) - 1):
        right_cards.append(cards[index])
    for index in range(len(left_cards)):
        shuffle_cards.append(right_cards[index])
        shuffle_cards.append(left_cards[index])
    cards = shuffle_cards.copy()
    shuffle_cards = []
    cards.append(last_card)
    cards.insert(0,top_card)
print(cards)

