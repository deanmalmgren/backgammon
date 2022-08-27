class Turn(object):
    def __init__(self, game):
        self.game = game

    @property
    def dice(self):
        return self.game.dice

    @property
    def player(self):
        return self.game.players[self.game.current_player]
