# Author: Daniel Reid Nelsen
# GitHub username: RNelsen
# Date: 3/9/23
# Description: This project is a simulation of a checkers game using classes
#              and objects.  

class OutofTurn(Exception):
    """Raise exception if a player moves out of turn"""
    pass

class InvalidSquare(Exception):
    """Raise exception if a player doesn't have a piece in the square"""
    pass

class InvalidPlayer(Exception):
    """Raise exception if the player doesn't exist"""
    pass

class Player():
    """The player class takes a player name and piece color."""

    def __init__(self, player_name, piece_color):
      
        self._player_name = player_name
        self._piece_color = piece_color
        self._king_count = 0
        self._triple_king_count = 0
        self._captured_pieces_count = 0

    def get_king_count(self):
        """Returns king count of player"""

        return self._king_count

    def get_tripe_king_count(self):
        """Returns the triple king count of player"""

        return self._triple_king_count

    def get_captured_pieces(self):
        """Returns the number of captured pieces"""

        return self._captured_pieces_count

    def get_player_name(self):
        """Method to get the players name for various methods and determine who
           won. Returns the players name"""

        return self._player_name

class Checkers:
    """The checker class"""

    def __init__(self):
        """Init method for the checkers class"""

        board = {(0,0):(),     (0,1):"White",(0,2):(),     (0,3):"White",(0,4):(),     (0,5):"White",(0,6):(),     (0,7):"White",
                 (1,0):"White",(1,1):(),     (1,2):"White",(1,3):(),     (1,4):"White",(1,5):(),     (1,6):"White",(1,7):(),
                 (2,0):(),     (2,1):"White",(2,3):(),     (2,3):"White",(2,4):(),     (2,5):"White",(2,6):(),     (2,7):"White",
                 (3,0):None,   (3,1):(),     (3,2):None,   (3,3):(),     (3,4):None,   (3,5):(),     (3,6):None,   (3,7):(),
                 (4,0):(),     (4,1):None,   (4,2):(),     (4,3):None,   (4,4):(),     (4,5):None,   (4,6):(),     (4,7):None,
                 (5,0):"Black",(5,1):(),     (5,2):"Black",(5,3):(),     (5,4):"Black",(5,5):(),     (5,6):"Black",(5,7):(),
                 (6,0):(),     (6,1):"Black",(6,2):(),     (6,3):"Black",(6,4):(),     (6,5):"Black",(6,6):(),     (6,7):"Black",
                 (7,0):"Black",(7,1):(),     (7,2):"Black",(7,3):(),     (7,4):"Black",(7,5):(),     (7,6):"Black",(7,7):(),}

        # board = {(0,0):(),     (0,1):"White",(0,2):(),     (0,3):"White",(0,4):(),     (0,5):"White",(0,6):(),     (0,7):"White",
        #          (1,0):"White",(1,1):(),     (1,2):"White",(1,3):(),     (1,4):None,(1,5):(),     (1,6):"White",(1,7):(),
        #          (2,0):(),     (2,1):"White",(2,3):(),     (2,3):"White",(2,4):(),     (2,5):"White",(2,6):(),     (2,7):"White",
        #          (3,0):None,   (3,1):(),     (3,2):"Black",   (3,3):(),     (3,4):None,   (3,5):(),     (3,6):None,   (3,7):(),
        #          (4,0):(),     (4,1):"White",(4,2):(),     (4,3):None,   (4,4):(),     (4,5):None,   (4,6):(),     (4,7):None,
        #          (5,0):"Black_King",(5,1):(),     (5,2):"Black",(5,3):(),     (5,4):"Black_King",(5,5):(),     (5,6):"Black",(5,7):(),
        #          (6,0):(),     (6,1):"Black",(6,2):(),     (6,3):"Black",(6,4):(),     (6,5):"Black",(6,6):(),     (6,7):"Black",
        #          (7,0):"Black",(7,1):(),     (7,2):"Black",(7,3):(),     (7,4):"Black",(7,5):(),     (7,6):"Black",(7,7):(),}

        self._square_layout = board
        self._turn = "Black"
        self._players = {}
        self._captured = 0
        self._moving = ""
        self._last_piece_moved = ""
        self._opponent_captured = False
        self._last_direction = ""

    def create_player(self, player_name, piece_color):
        """Create players for the game.  Creates an object from the Player class.  
        Puts these objects in a dictionary."""

        self._players[player_name] = Player(player_name, piece_color)
        return self._players.get(player_name)

    def change_board(self, new_board):
        """Method to change the board structure for testing purposes"""

        self._square_layout = new_board

    def get_turn(self):
        """Method to return who's turn it is"""

        return self._turn

        # checker_type = checker_type[0:5]
        # if checker_type == "Black":
        #     return "Black"
        # else:
        #     return "White"

    def set_turn(self):
        """Method to set who's turn it is. Called after a successful move is
           made and no pieces are captured. This method is not called after 
           a captures, because a capture means the player has another turn"""

        if self._turn == "Black":
            self._turn = "White"
        else:
            self._turn = "Black"

        self._opponent_captured = False

    def set_king(self, location, player_name):
        """Sets the piece to king after it reaches the opposite side of the 
           board.  Nothing is returned from this method"""

        if self._square_layout.get(location) == "White":
            self._square_layout.update({location:"White_King"})
        else:
            self._square_layout.update({location:"Black_King"})
        
        self._players.get(player_name)._king_count += 1

    def set_triple_king(self, location, player_name):
        """Set king to triple king after a king reaches its home row.  
           Nothing is returned from this method"""

        if self._square_layout.get(location) == "White_King":
            self._square_layout.update({location:"White_Triple_King"})
        else:
            self._square_layout.update({location:"Black_Triple_King"})

        self._players.get(player_name)._triple_king_count += 1

    def set_moving_piece(self, start):
        """Helper method for the class.  This sets what piece is moving, 
           regular, king, or triple king.  Nothing is returned from this method"""

        self._moving = self._square_layout.get(start)

    def get_moving(self):
        """Helper method for the class to see which piece we are moving.  
           This is needed by play_game to determine if the piece is able to 
           move backwards or forwards based on color.  This method returns the
           game piece type, regular, king, or triple king"""

        return self._moving

    def play_game(self, player_name, start, finish):
        """Method for moving pieces on the checkers board.  
           See description below for explanation.  
           Final return is how many pieces were captured during the move"""
        
        captured = 0
        moving_forward_backward = None
        moving_left_right = None
        checker_type = self._square_layout.get(start)
        white_edge_list = [(0,1), (0,3), (0,5), (0,7)]
        black_edge_list = [(7,0), (7,2), (7,4) ,(7,6)]
        jumping = False
        
        #unpack coordinates tuple
        (row_start, column_start) = start
        (row_finish, column_finish) = finish

        #determining which way the piece moves
        if row_start - row_finish > 0:
            moving_forward_backward = "forward"
        else:
            moving_forward_backward = "backward"
        
        # setting last direction moving to check if empty cells exist forward of 
        # backward of the last piece moved.
        self._last_direction = moving_forward_backward

        if column_start - column_finish < 0:
            moving_left_right = "right"
        else:
            moving_left_right = "left"

        #detect if player is jumping
        if abs(row_start - row_finish) >= 2:
            jumping = True

        # check to see if the player exists.
        if self._players.get(player_name) == None:
            raise InvalidPlayer

        if checker_type == None:
            raise InvalidSquare

        # checks to see if the square is in the list for the player
        if (self._square_layout.get(start)[0:5]) != self._players.get(player_name)._piece_color:
            raise InvalidSquare        
        else:
            self.set_moving_piece(start)

        # check to see if it is the players turn
        if self._players.get(player_name)._piece_color != self.get_turn():
            raise OutofTurn
        if self._opponent_captured == True and start != self._last_piece_moved and self.can_jump() == True:
            raise OutofTurn

        # check to see if the starting square is on the board
        if start not in self._square_layout:
            raise InvalidSquare

        # checks that the piece is moving in the correct direction
        if (checker_type != "Black_King" and checker_type != "White_King" and 
            checker_type != "Black_Triple_King" and checker_type != "White_Triple_King"):
            if (self._players.get(player_name)._piece_color == "Black"    
                and moving_forward_backward == "backward"):
                raise InvalidSquare
            elif (self._players.get(player_name)._piece_color == "White" 
                and moving_forward_backward == "forward"):
                raise InvalidSquare

        # checks that the destination is empty and moves the piece to that spot
        #if jumping == False and (checker_type == "White" or checker_type == "Black"):
        if jumping == False:
            if self._square_layout.get(finish) == None:
                  self._square_layout.update({finish:self._square_layout.get(start)}) 
                  self._square_layout.update({start:None})
                  self.set_turn()
            else:
                raise InvalidSquare

        #this is for jumping and capturing pieces for regular pieces
        elif jumping == True and (self._moving == "White" or self._moving == "Black"):
            if self._square_layout.get(finish) == None:
                if ((moving_left_right == "left" and moving_forward_backward == "forward") and 
                (self._square_layout.get((row_start - 1, column_start - 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_start - 1, column_start - 1):None})

                elif ((moving_left_right == "right" and moving_forward_backward == "forward") and 
                (self._square_layout.get((row_start - 1, column_start + 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_start - 1, column_start + 1):None})

                elif ((moving_left_right == "left" and moving_forward_backward == "backward") and 
                (self._square_layout.get((row_start + 1, column_start - 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_start + 1, column_start - 1):None})

                elif ((moving_left_right == "right" and moving_forward_backward == "backward") and 
                (self._square_layout.get((row_start + 1, column_start - 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_start + 1, column_start - 1):None})
                self._players.get(player_name)._captured_pieces_count += captured
                self.set_last_piece_moved(finish)
            else:
                raise InvalidSquare

        # Movement of King and Triple King with jumping and capturing
        if jumping == True and (self._moving != "Black" and self._moving != "White"):
            if self._square_layout.get(finish) == None:
                if ((moving_left_right == "left" and moving_forward_backward == "forward") and 
                (self._square_layout.get((row_start - 1, column_start - 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_start - 1, column_start - 1):None})

                elif ((moving_left_right == "right" and moving_forward_backward == "forward") and 
                (self._square_layout.get((row_finish + 1, column_finish - 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_finish + 1, column_finish - 1):None})

                elif ((moving_left_right == "left" and moving_forward_backward == "backward") and 
                (self._square_layout.get((row_start + 1, column_start - 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_start + 1, column_start - 1):None})

                elif ((moving_left_right == "right" and moving_forward_backward == "backward") and 
                (self._square_layout.get((row_start + 1, column_start - 1)) != self._players.get(player_name)._piece_color)):
                    captured = self.count_captured(start, finish)
                    self._square_layout.update({finish:self._moving}) 
                    self._square_layout.update({start:None})
                    self._square_layout.update({(row_start + 1, column_start - 1):None})
                self._players.get(player_name)._captured_pieces_count += captured
                self.set_last_piece_moved(finish)
            else:
                raise InvalidSquare

        # checks of the piece is against the edge and make it a king or triple king if required
        if finish in white_edge_list and self._moving == "Black":
            self.set_king(finish, player_name)

        elif finish in black_edge_list and self._moving == "Black_King":
            self.set_triple_king(finish, player_name)

        elif finish in black_edge_list and self._moving == "White":
            self.set_king(finish, player_name)

        elif finish in white_edge_list and self._moving == "White_King":
            self.set_triple_king(finish, player_name)
    
        return captured

    def can_jump(self):
        """This is a check for the last piece that is moved to see if it can jump 
        and capture an opponent's piece.  If it can then it returns True and the 
        player must move that piece"""
        
        can_jump = False

        (row, column) = self._last_piece_moved

        if self._last_direction == "forward":
            if self._square_layout.get((row - 2, column - 2)) == None:
                can_jump = True
            elif self._square_layout.get((row - 2, column + 2)) == None:
                can_jump = True
        elif self._last_direction == "backward":
            if self._square_layout.get((2 + row, column - 2)) == None:
                can_jump = True
            elif self._square_layout.get((2 + row, 2 + column)) == None:
                can_jump = True

        return can_jump

    def set_last_piece_moved(self, finish_location):
        """Method to record the finishing location of the last piece that 
        captured an opponent piece.  Used in determining whether or not the 
        correct player is playing next.  Nothing is returned from this method"""

        self._last_piece_moved = finish_location
        self._opponent_captured = True


    def count_captured(self, start, finish):
        """Method to see how many pieces will be captured.  This is called from 
           the play_game method and will return how many pieces will be captured 
           after the move is finished.  This returns the number of captured 
           pieces to play_game"""

        captured = 0

        #unpack coordinates tuple
        (row_start, column_start) = start
        (row_finish, column_finish) = finish

        row_count = row_start
        column_count = column_start

        #determining which way the piece moves
        if row_start - row_finish > 0:
            moving_forward_backward = "forward"
        else:
            moving_forward_backward = "backward"

        if column_start - column_finish < 0:
            moving_left_right = "right"
        else:
            moving_left_right = "left"

        #determines how many are captured during the move.  Useful for Triple Kings
        #but can be used for any piece
        if moving_left_right == "right" and moving_forward_backward == "forward":
            row_count -= 1
            column_count += 1
            while (row_count, column_count) != finish:
                if self._square_layout.get((row_count, column_count)) != None:
                    captured += 1 
                column_count += 1
                row_count -= 1
        elif moving_left_right == "left" and moving_forward_backward == "forward":
            row_count -= 1
            column_count -= 1
            while (row_count, column_count) != finish:
                if self._square_layout.get((row_count, column_count)) != None:
                    captured += 1 
                column_count -= 1
                row_count -= 1
        elif moving_left_right == "left" and moving_forward_backward == "backward":
            row_count += 1
            column_count -= 1
            while (row_count, column_count) != finish:
                if self._square_layout.get((row_count, column_count)) != None:
                    captured += 1 
                column_count -= 1
                row_count += 1
        elif moving_left_right == "right" and moving_forward_backward == "backward":
            row_count += 1
            column_count += 1
            while (row_count, column_count) != finish:
                if self._square_layout.get((row_count, column_count)) != None:
                    captured += 1 
                column_count += 1
                row_count += 1

        return captured

    def get_checker_details(self, location):
        """Gets the details about a square on the checker board.  
           This will return what piece is occupying a valid square.  
           Returns None if no piece is on the square."""

        (row, column) = location

        if (row < 0 or row > 7) or (column < 0 or column > 9):
            raise InvalidSquare

        if self._square_layout.get(location) == None:
            return None
        else:
            return self._square_layout.get(location)

    def print_board(self):
        """Prints the current board layout.  Returns the current board layout 
           in the form of a list for each row and then those lists are in a 
           list for the entire board """

        board_layout = []
        row = []
        counter = 0

        # Converting from the board dictionary to a list of lists
        for key, value in self._square_layout.items():
            if value == ():
                row.append(None)
            else:
                row.append(value)
            counter += 1
            if counter == 8:
                board_layout.append(row)
                row = []
                counter = 0

        return board_layout

    def game_winner(self):
        """Returns either the name of the player who won the game or "Game Not
        has not ended"""

        for person in self._players:
            if self._players.get(person).get_captured_pieces() == 12:
                return person
        
        return "Game has not ended"


def main():
    """Main function to create the Checkers game"""

    game = Checkers()
    player1 = game.create_player("Reid", "White")
    player2 = game.create_player("Melany", "Black")
    print(game.play_game(player2.get_player_name(), (5,2), (4,3)))
    print(game.play_game(player2.get_player_name(), (4,1), (2,3)))
    print(game.play_game(player2.get_player_name(), (5,2), (4,1)))
    # print(player2.get_captured_pieces())
    # print(player2.get_king_count())
    # print(game.game_winner())

if __name__ == '__main__':
    main()

    