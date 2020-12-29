from board.py import Board


class Player:
    """ a player for a Connect Four game
    """   
    def __init__(self, checker) :
        """constructs a new Board 
        """
        self.checker=checker
        self.num_moves=0
        
    def __repr__(self):
        """ Returns a string representation of player
        """
        return 'Player '+ self.checker
    
    def opponent_checker(self):
        """returns a one-character string representing the 
        checker of the Player object’s opponent
        """
        if self.checker=='X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the column where
        the player wants to make the next move.
        """
        self.num_moves+=1
        while True:
            col=int(input('Enter a column: '))
            if b.can_add_to(col)==True:
                return col
            else:
                print('Try again!')

