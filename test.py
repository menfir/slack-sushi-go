import Deck
import Game

def main():
    game = Game.Game()
    game.addPlayer("Jeroen")
    game.addPlayer("Wouter")
    game.start()


if __name__ == "__main__":
    main()