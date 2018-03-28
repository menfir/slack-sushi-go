import Card
from random import shuffle
class Deck:

    def __init__(self):
        self.cards = []
        for x in range(0, 14):
            self.add(Card.Card("tempura"))
        for x in range(0, 14):
            self.add(Card.Card("sashimi"))
        for x in range (0, 14):
            self.add(Card.Card("dumpling"))
        for x in range(0, 12):
            self.add(Card.Card("2 sushi rolls"))
        for x in range(0, 8):
            self.add(Card.Card("3 sushi rolls"))
        for x in range (0, 6):
            self.add(Card.Card("1 sushi roll"))
        for x in range(0, 10):
            self.add(Card.Card("salmon nigiri"))
        for x in range(0, 5):
            self.add(Card.Card("squid nigiri"))
        for x in range (0, 5):
            self.add(Card.Card("egg nigiri"))
        for x in range(0, 10):
            self.add(Card.Card("pudding"))
        for x in range(0, 6):
            self.add(Card.Card("wasabi"))
        for x in range (0, 4):
            self.add(Card.Card("chopsticks"))
        self.shuffle()

    def add(self, card):
        self.cards.append(card)

    def shuffle(self):
        for i in range (0, 7):
            shuffle(self.cards)

    def myprint(self):
        for c in self.cards:
            c.myprint()
    
    def draw(self, x):
        drawn_cards = []
        for i in range (0, x):
            drawn_cards.append(self.cards.pop())
        return drawn_cards
