
card_strengths = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}


class Hand:
    def __init__(self, line):
        self.cards = line.split()[0]
        self.bid = int(line.split()[1])
        self._type = self._get_type()

    def __eq__(self, other_hand):
        if isinstance(other_hand, Hand):
            return self.cards == other_hand.cards
        return False

    def __lt__(self, other_hand):
        if isinstance(other_hand, Hand):
            # self.value < other.value
            if self._type < other_hand._type:
                return True
            elif self._type > other_hand._type:
                return False
            else:
                for i in range(len(self.cards)):
                    if card_strengths[self.cards[i]] < card_strengths[other_hand.cards[i]]:
                        return True
                    elif card_strengths[self.cards[i]] > card_strengths[other_hand.cards[i]]:
                        return False
            return NotImplemented

    def __str__(self):
        return self.cards

    def _get_type(self) -> int:
        occs = {}
        jokers = len([x for x in self.cards if x == "J"])
        for c in self.cards:
            if c != "J":
                occ = self.cards.count(c)
            else:
                continue
            if occ + jokers == 5:
                return 6
            elif occ + jokers == 4:
                return 5
            occs[c] = occ

        if 3 in occs.values() and 2 in occs.values():
            if jokers == 2 or jokers == 3:
                return 6
            return 4
        elif 3 in occs.values():
            if jokers != 0:
                return 3 + jokers + 1
            else:
                return 3
        elif list(occs.values()).count(2) == 2:
            if jokers != 0:
                return 2 + jokers + 1
            else:
                return 2
        elif 2 in occs.values():
            return 1 + jokers
        else:
            return 0 + jokers


def main():
    with open("input.txt", "r") as file:
        hands = []
        for line in file:
            hands.append(Hand(line))

        hands = sorted(hands)
        total_winnings = 0
        for i in range(len(hands)):
            total_winnings += (hands[i].bid * (i+1))

        print("====")
        print(total_winnings)


if __name__ == '__main__':
    main()



