

with open("input.txt", "r") as file:
    card_map = {}
    card_id = 0
    cards = file.readlines()
    for i in range(len(cards)):
        card_map[i + 1] = 1

    for card in cards:
        card_id += 1
        card = card.split(": ")[1:][0]
        winning_numbers = [int(x) for x in card.split("|")[0].split()]
        my_numbers = [int(x) for x in card.split("|")[1].split()]
        cards_won = 0
        for number in my_numbers:
            if number in winning_numbers:
                cards_won += 1

        for i in range(1, cards_won + 1):
            card_map[card_id + i] += card_map[card_id]

    total_sum = 0
    for card_amount in card_map.values():
        total_sum += card_amount
    print(total_sum)
