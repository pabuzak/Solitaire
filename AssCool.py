# CardPile Class
# represents a pile of cards
# has functions for adding, removing and inspecting cards in the pile
class CardPile:
    def __init__(self):
        self.item = []

    def add_top(self, item):
        self.item.insert(0, item)

    def add_bottom(self, item):
        self.item.append(item)

    def remove_top(self):
        return self.item.pop(0)

    def remove_bottom(self):
        return self.item.pop()

    def size(self):
        return len(self.item)
    
    # displays the top card
    def peek_top(self):
        return self.item[0]

    # displays the bottom card
    def peek_bottom(self):
        return self.item[-1]
    
    # string representation of the card pile and its contents
    def print_all(self, index):
        if index == 0:
            string = ""
            for i in self.item:
                if i == self.item[0]:
                    string += str(i) + " "
                else:
                    string += "*" + " "
            return string[:-1]
            
        else:
            string = ""
            for i in self.item:
                string += str(i) + " "
            return string[:-1]

# Solitaire Class
# the main game which manages multiple piles
# provides inputs for the user to play the game
# provides rules for the user
class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])

    def get_pile(self, i):
        return self.piles[i]

    # displays the current state of the game
    def display(self):
        card_pile = self.num_piles
        for i in range(card_pile):
            pile = self.piles[i]
            count = pile.size()
            print(f"{i}: ({count} cards): {self.piles[i].print_all(i)}")

    # move a card to a pile and checks if valid
    def move(self, p1, p2):
        if p1 == p2 == 0 and self.piles[0].size() > 0:
            card = self.piles[0].peek_top()
            self.piles[0].remove_top()
            self.piles[0].add_bottom(card)

        elif p1 == 0 and p2 > 0:
            if self.piles[0].size() > 0:
                card1 = self.piles[0].peek_top()
                card2 = self.piles[p2].peek_bottom() if self.piles[p2].size() > 0 else None
                if card2 is None:
                    self.piles[p2].add_bottom(card1)
                    self.piles[0].remove_top()
                elif card2 is not None and card1 == card2 - 1:
                    self.piles[0].remove_top()
                    self.piles[p2].add_bottom(card1)

        elif p1 > 0 and p2 > 0:
            if self.piles[p1].size() > 0:
                card1 = self.piles[p1].peek_top()
                card2 = self.piles[p2].peek_bottom() if self.piles[p2].size() > 0 else None
                if card2 is None:
                    pass
                elif card2 is not None and card1 == card2 - 1:
                    while self.piles[p1].size() > 0:
                        card = self.piles[p1].remove_top()
                        self.piles[p2].add_bottom(card)

    # check if the game is completed or not
    def is_complete(self):
        if self.piles[0].size() > 0:
            return False

        for i in range(1, self.num_piles):
            pile = self.piles[i].item
            if pile == sorted(pile, reverse=True) and len(pile) == self.num_cards:
                return True
        
        return False

    # print rules
    def rules(self):
        print("")
        print("Welcome to Solitaire!")
        print("The goal of the game is to arrange all cards in descending order.")
        print("You can move cards from pile to pile to build sequences in descending order.")
        print("Only move a card to the bottom of a pile if it's one less than the last card in the pile.")
        print("A higher number card can be placed on top of a lower number card.")
        print("You win once all the cards are arranged accordingly.")
        print("")

    def play(self):
        while True:
            print("********************** NEW GAME *****************************")
            self.rules()
            move_number = 1

            while move_number <= self.max_num_moves and not self.is_complete():
                self.display()
                print("Round", move_number, "out of", self.max_num_moves, end = ": ")
                pile1 = int(input("Move from pile no.: "))
                print("Round", move_number, "out of", self.max_num_moves, end = ": ")
                pile2 = int(input("Move to pile no.: "))
                if (pile1 >= 0 and pile2 >= 0 and pile1 < self.num_piles
                    and pile2 < self.num_piles):
                        self.move(pile1, pile2)
                move_number += 1

            if self.is_complete():
                print("You Win in", move_number - 1, "steps!")

                # asks user to play again
                play_again = input("Do you want to play another game? (yes/no): ")
                if play_again.lower() != 'yes':
                    break

            else:
                print("You Lose!\n")
