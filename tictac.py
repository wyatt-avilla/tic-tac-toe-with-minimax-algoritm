# author: Larissa Munishkina
# date: May 21, 2020
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

from board import Board
from player import SmartAI
from player import MiniMax
from player import Ai
from player import Player

print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    player1 = Player("Bob", "X")                  # change the classes of the player1 and player2 to adjust the functionality 
    player2 = SmartAI("Alice", "O")               # (Player, Ai, MiniMax, or SmartAI)
    turn = True                                   # currently set up to have the user play against SmartAI
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N]\n").upper()
    if (ans != "Y"):
        break
print("Goodbye!")