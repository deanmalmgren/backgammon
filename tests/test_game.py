import unittest

from nose2.tools import params

from backgammon import Game

class TestGame(unittest.TestCase):
    def test_game_value(self):
        game = Game()
        self.assertEqual(game.game_value, 1)

    @params(1, 'a')
    def test_not_player(self, player1):
        with self.assertRaises(TypeError):
            game = Game(player1)
