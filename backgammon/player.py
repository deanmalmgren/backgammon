class Player(object):

    def __init__(self, game):
        self.game = game

    @property
    def board(self):
        return self.game.board

    @property
    def dice(self):
        return self.game.dice

    def make_move(self):
        return


class RandomPlayer(Player):
    pass
