
from backgammon import Board
from backgammon import Game
from backgammon import Dice


game = Game()

for turn in game.turn():
    turn.dice
    turn.player.make_move()
    print(game.board)

print(game.winner)
