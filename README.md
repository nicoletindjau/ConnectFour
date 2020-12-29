# ConnectFour
Connect Four written using Object-Oriented Principles in Python. The game could be played between 2 human players, 2 computer players or a computer player vs a human player.

How to run/play:
1. Choose two players to play. There are 3 types of players in this code: A human player, A random player, and an AI player.
A human player would ask the player which column to play next, A random player randomly selects a column to play, while an AI player thinks about its future moves and looks ahead.

2. A human player: Player('X') or Player('O')
   A random player: RandomPlayer('X') or RandomPlayer('O')
   An Ai player: AIPlayer('X', tiebreak, lookahead) or AIPlayer('O', tiebreak, lookahead)
   (tiebreak: 'LEFT', 'RIGHT', or 'RANDOM'- specify the player’s tiebreaking strategy. lookahead: an integer specifying how many moves the player looks ahead in order to evaluate possible moves, thus, the higher the lookahead the smarter the AI)
   
3. After selecting your players you can run aiPlayer.py and in the console write 
'connect_four(Player1, Player2)'
(where Player1 and player 2 are one of the players in step 2)

eg. to play between two humans:
'connect_four(Player('X'), Player('O'))'
eg. to play between against an AI with a lookahead 5 and a left tiebreaker:
'connect_four(Player('X'), AIPlayer('O', 'LEFT', 5))'
eg. to see an AI with a lookahead 5 and a left tiebreaker play against a random player
'connect_four(RandomPlayer('X')), AIPlayer('O', 'LEFT', 5))'




