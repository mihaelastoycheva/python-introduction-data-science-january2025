cards = input().split()
number_of_shuffles = int(input())

half = len(cards) // 2

for _ in range(number_of_shuffles):
    top_half = cards[:half]  # slicing: from 0 to half
    bottom_half = cards[half:]  # slicing: from half to the end

    shuffled_cards = []
    for i in range(half):
        shuffled_cards.append(top_half[i])
        shuffled_cards.append(bottom_half[i])

    cards = shuffled_cards

print(cards)