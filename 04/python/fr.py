class Card:
    def __init__(self, line) -> None:
        card_side, your_numbers = line.strip().split("|")
        self.id  = int(card_side.split(":")[0].split(" ")[-1])
        self.card_numbers = [card_number for card_number in card_side.split(":")[1].strip().split(" ") if card_number]
        self.your_numbers = [your_number for your_number in your_numbers.strip().split(" ") if your_number]
        self.count = 1
        
        
    def get_winning_numbers_count(self):
        return len([number for number in self.your_numbers if number in self.card_numbers])

    def get_card_value(self):
        return int(min(1,self.get_winning_numbers_count()) * 2**(self.get_winning_numbers_count()-1))
    

def solve_1(file):
    with open(file) as f:
        print(sum([Card(line).get_card_value() for line in f]))


def solve_2(file):
    with open(file) as f:
        cards = [Card(line) for line in f]
        card_count = len(cards)
        for card in cards:
            # for each card type
            for i in range(card.count):
                # for each copy of the card
                new_card_amount = card.get_winning_numbers_count()
                # add count to subsequent cards
                for j in range(card.id, min(card.id+new_card_amount, card_count)):
                    cards[j].count += 1 
    print(sum([card.count for card in cards]))
        
if __name__ == "__main__":
    solve_1("inp_ex")
    solve_1("inp")
    solve_2("inp_ex")
    solve_2("inp")