import unittest

from backgammon import Game

class TestGame(unittest.TestCase):
    def test_game_value(self):
        game = Game()
        self.assertEqual(game.game_value, 1)
