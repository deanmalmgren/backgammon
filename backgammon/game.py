import random

from .player import RandomPlayer, Player


class Game(object):

    def __init__(self, player1=None, player2=None):
        self.game_value = 1

        if player1 is None:
            player1 = RandomPlayer()
        if player2 is None:
            player2 = RandomPlayer()
        if not isinstance(player1, Player):
            raise TypeError('player1 is not a Player')
        if not isinstance(player2, Player):
            raise TypeError('player2 is not a Player')
        self.players = [player1, player2]
