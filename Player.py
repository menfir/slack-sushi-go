class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.played_cards = []
        self.played_pudding = []

    
    def deal(self, cards):
        for card in cards:
            self.hand.append(card)
    
    def myprint(self):
        print self.name
        print self.hand
    
    def __str__(self):
        s = self.name 
        s += "\nhand: " + ", ".join(map(str, self.hand))
        s += "\nplayed cards: " + ", ".join(map(str, self.played_cards))
        s += "\nplayed pudding: " + str(len(self.played_pudding))
        return s

    def play(self, index):
        if index <= len(self.hand):
            card = self.hand.pop(index)
            if card.isPudding():
                self.played_pudding.append(card)
            else:
                self.played_cards.append(card)


