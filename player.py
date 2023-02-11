from random import randint
from board import Board
import math


class Player:    
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
    def get_sign(self):
        return self.sign
            # return an instance sign
    def get_name(self):
        return self.name
            # return an instance name
    def choice_format(self, input):
        if len(input) == 2:
            if input[0].isalpha() and input[1].isdigit():
                if int(input[1]) in range(1,4):
                    if input[0] in ["A", "B", "C"]:
                        return True
                    
    def choose(self, board):   # allows the player to choose their move
        done = False
        while not done:
            choice = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]:").upper()
            if self.choice_format(choice) == True and board.isempty(choice) == True: # makes move if format of user input is correct, otherwise the prompt is reprinted
                board.set(choice, self.sign)
                done = True
            else:
                print("You did not choose correctly.")

    def opponent_sign(self):
        if self.sign == "X":
            return "O"
        if self.sign == "O":
            return "X"

class Ai(Player):
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
    def choose(self, board): # randomly selects a move from available cells
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        done = False
        while not done: 
            options = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
            randomchoice = options[randint(0,8)]
            if board.isempty(randomchoice) == True:
                board.set(randomchoice, self.sign)
                done = True
            else:
                continue

class MiniMax(Ai):
    def choose(self, board):
        bestscore = -math.inf
        optmove = ""
        moves = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        for move in moves:
            if board.isempty(move) == True:
                board.set(move, self.sign)
                score = MiniMax.minimax(self, board, False)
                board.resetcell(move)
                if score > bestscore:
                    bestscore = score
                    optmove = move
        board.set(optmove, self.sign) 

    def minimax(self, board, self_player):   # minimax algorithm implementation
        optmove = "A1"
        moves = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        if board.isdone() == True: # base cases
            if board.get_winner() == self.sign:              # win
                return 10
            elif board.get_winner() == "TIE":                # tie
                return 0
            elif board.get_winner() == self.opponent_sign(): # loss
                return -10
            
        # recursively makes moves until there are none left
        if self_player == True: # playing as self
            maxscore = -math.inf
            for move in moves:
                if board.isempty(move) == True:
                    board.set(move, self.sign)
                    score = MiniMax.minimax(self, board, False)  # recursive call with opponent as player
                    if score > maxscore:
                        maxscore = score
                    board.resetcell(move)
            return maxscore

        if self_player == False: # playing as opponent
            minscore = math.inf
            for move in moves:
                if board.isempty(move) == True:
                    board.set(move, self.opponent_sign())
                    score = MiniMax.minimax(self, board, True)   # recursive call with self as player
                    if score < minscore:
                        minscore = score
                    board.resetcell(move)
            return minscore

class SmartAI(MiniMax): 
    def choose(self, board):  # minimax algorithm, except with the first move being randomly selected
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        starts = ["A1", "C1", "B2", "A3", "C3"]
        if len(board.getopencells()) > 7:
            x = randint(0,4) 
            if board.isempty(starts[x]):
                board.set(starts[x], self.sign)
            else: 
                board.set(starts[x+1 % len(starts)], self.sign)
            
        else:
            bestscore = -math.inf
            optmove = ""
            moves = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
            print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            for move in moves:
                if board.isempty(move) == True:
                    board.set(move, self.sign)
                    score = MiniMax.minimax(self, board, False)
                    board.resetcell(move)
                    if score > bestscore:
                        bestscore = score
                        optmove = move
            board.set(optmove, self.sign)