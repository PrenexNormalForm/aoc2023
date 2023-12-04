class Scratchoff:
    def __init__(self, definition: str) -> None:
        card_num, definition = definition.split(":")
        self.id = int(card_num.split()[-1])
        self.winning_numbers, self.having_numbers = (
            set(int(n) for n in num_list.split()) for num_list in definition.split("|")
        )

    def matching_numbers(self):
        return self.winning_numbers & self.having_numbers

    def winnings(self) -> int:
        matching_numbers = self.matching_numbers()
        if not matching_numbers:
            return 0
        return int(2 ** (len(self.matching_numbers()) - 1))


if __name__ == "__main__":
    # problem 1
    with open("day/04/input.txt") as f:
        total_winnings = 0
        for line in f:
            scratchoff = Scratchoff(line)
            total_winnings += scratchoff.winnings()
        print(f"Total winnings: {total_winnings}")

    # problem 2
    with open("day/04/input.txt") as f:
        num_duplicates = [0] * 10
        total_unique_cards = 0
        for line_no, line in enumerate(f):
            total_unique_cards += 1
            num_duplicates[line_no] += 1
            num_duplicates.append(0)
            card = Scratchoff(line)
            for offset in range(1, len(card.matching_numbers()) + 1):
                num_duplicates[line_no + offset] += num_duplicates[line_no]
        print(f"Total cards: {sum(num_duplicates[:total_unique_cards])}")
