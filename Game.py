import Deck
import Player

playercount = dict({"2":10, "3":9,"4":8,"5":7})

class Game:    
    
    def __init__(self):
        self.deck = Deck.Deck()
        self.players  = []
        self.round = 0
        self.game = 0
    
    def addPlayer(self, name):
        self.players.append(Player.Player(name))
    
    def nrOfPlayers(self):
        return str(len(self.players))

    def start(self):
        self.game += 1
        self.round = playercount[self.nrOfPlayers()]
        for player in self.players:
            player.deal(self.deck.draw(playercount[self.nrOfPlayers()]))
            #print(player)
        
