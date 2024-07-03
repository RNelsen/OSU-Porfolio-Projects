# Author: Daniel Reid Nelsen
# GitHub username: RNelsen
# Date: 3/9/23
# Description: This is a test file for the CheckerGame.py file

import unittest
from CheckersGame import Checkers, Player, InvalidPlayer, OutofTurn

class CheckersGameTest(unittest.TestCase):

    def test_1(self):
        """Testing that the creation of from the Checkers class is creating an 
        player object from Player class"""

        game = Checkers()
        player1 = game.create_player("player_1", "Black")
        self.assertIsInstance(player1, Player)

    def test_2(self):
        """Testing that a jump and capture returns the number of captured pieces"""

        game = Checkers()
        player1 = game.create_player("player_1", "Black")
        player2 = game.create_player("player_2", "White")
        game.play_game(player1.get_player_name(), (5,2), (4,3))
        game.play_game(player2.get_player_name(), (2,5), (3,4))
        self.assertEqual(game.play_game(player1.get_player_name(), (4,3), (2,5)), 1)

    def test_3(self):
        """Testing if a wrong player is passed to the Checkers class that the 
        InvalidPlayer exception is raised"""

        game = Checkers()
        player1 = game.create_player("player_1", "Black")
        
        with self.assertRaises(InvalidPlayer):
            game.play_game("player_3", (5,2), (4,3))

    def test_4(self):
        """Testing if a player plays out of turn that OutofTurn exception
        will be raised"""

        game = Checkers()       
        player1 = game.create_player("player_1", "Black")
        player2 = game.create_player("player_2", "White")
        
        with self.assertRaises(OutofTurn):
            game.play_game("player_2", (2,3), (3,2))

    def test_5(self):
        """
        Testing that triple king jumping and capturing returns the correct 
        amount of captured pieces.  Since the Checkers class setups up the initial 
        board this test needs to override the self._square_layout before the test.  
        This way long game play doesn't need to take place to set up the 
        board for the test.
        """

        game = Checkers()
        board = {(0,0):(),     (0,1):"White",(0,2):(),     (0,3):"White",(0,4):(),     (0,5):"White",(0,6):(),     (0,7):"White",
                 (1,0):"White",(1,1):(),     (1,2):"White",(1,3):(),     (1,4):None,(1,5):(),     (1,6):"White",(1,7):(),
                 (2,0):(),     (2,1):"White",(2,3):(),     (2,3):None,(2,4):(),     (2,5):"White",(2,6):(),     (2,7):"White",
                 (3,0):None,   (3,1):(),     (3,2):"White",   (3,3):(),     (3,4):None,   (3,5):(),     (3,6):None,   (3,7):(),
                 (4,0):(),     (4,1):"White",(4,2):(),     (4,3):None,   (4,4):(),     (4,5):None,   (4,6):(),     (4,7):None,
                 (5,0):"Black_Triple_King",(5,1):(),     (5,2):"Black",(5,3):(),     (5,4):"Black_King",(5,5):(),     (5,6):"Black",(5,7):(),
                 (6,0):(),     (6,1):"Black",(6,2):(),     (6,3):"Black",(6,4):(),     (6,5):"Black",(6,6):(),     (6,7):"Black",
                 (7,0):"Black",(7,1):(),     (7,2):"Black",(7,3):(),     (7,4):"Black",(7,5):(),     (7,6):"Black",(7,7):(),}
        game.change_board(board)
        player1 = game.create_player("player_1", "Black")
        self.assertEqual(game.play_game(player1.get_player_name(), (5,0), (2,3)), 2)


if __name__ == '__main__':
    unittest.main()

