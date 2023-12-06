with open("input.txt", "r") as cards:
    total_sum = 0
    for card in cards:
        card = card.split(": ")[1:][0]
        winning_numbers = [int(x) for x in card.split("|")[0].split()]
        my_numbers = [int(x) for x in card.split("|")[1].split()]
        current_sum = 1
        for number in my_numbers:
            if number in winning_numbers:
                current_sum *= 2
        total_sum += int(current_sum/2)
    print(total_sum)