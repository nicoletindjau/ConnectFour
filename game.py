from board import Board
from player import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """ process a move
    input: Player object p for the player whose move is being processed, 
    and a Board object b for the board
    """
    p1=p.__repr__()
    print(p1+"'s turn")
    next_move_col= p.next_move(b)
    b.add_checker(p.checker, next_move_col)
    print()
    print(b)
    
    if b.is_win_for(p.checker)==True:
        print(p1 ,'wins in', p.num_moves,'moves. \nCongratulations!')
        return True
    elif b.is_full()==True and b.is_win_for(p.opponent_checker())==False \
    and b.is_win_for(p.checker)==False:
        print ("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    """unintelligent computer player that chooses at random from the available columns.
    """
    def next_move(self, b):
        """Rather than asking the user for the next move, this version of next_move
        should choose at random from the columns in the board b that are not yet full
        """
        self.num_moves+=1
        available_col=[]
        for i in range(b.width):
            if b.can_add_to(i):
                available_col+=[i]
        move=random.choice(available_col)
        return move
        
