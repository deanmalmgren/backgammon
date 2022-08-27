import random

from .player import RandomPlayer, Player
from .dice import Dice
from .turn import Turn
from .board import Board


class Game(object):

    def __init__(self, Player1=None, Player2=None):
        self.game_value = 1
        self.dice = Dice()
        self.board = Board()
        self.current_player = None
        if Player1 is None:
            Player1 = RandomPlayer
        if Player2 is None:
            Player2 = RandomPlayer
        if not issubclass(Player1, Player):
            raise TypeError('Player1 is not a Player')
        if not issubclass(Player2, Player):
            raise TypeError('Player2 is not a Player')
        self.players = [Player1(self), Player2(self)]
        self.winner = None

    def init_turn(self):
        self.current_player = None
        while self.current_player is None:
            self.dice.roll()
            print(self.dice)
            if self.dice.is_doubles():
                self.game_value *= 2
            else:
                if self.dice[0] > self.dice[1]:
                    self.current_player = 0
                else:
                    self.current_player = 1
        print(self.current_player+1, self.game_value)
        return Turn(self)

    def iter_turn(self):
        yield self.init_turn()
