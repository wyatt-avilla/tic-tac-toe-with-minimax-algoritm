class Board:
    def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
        self.sign = " "
        self.size = 3
        self.board = [" " for x in range(self.size**2)]
            
        self.winner = ""
    def get_size(self, size): #returns board size
        self.size = size 

    def get_winner(self): #returns sign of winner (O or X)
        return self.winner

    def get_board_state(self):
        x = self.board
        return x
    
    def set(self, cell, sign):  #update cell on board with given sign
        cells = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        self.board[cells.index(cell)] = sign

    def isempty(self, cell):  #checks if cell is empty
        cells = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        cellindex = cells.index(cell)
        if self.board[cellindex] == " ":
            return True


    def resetcell(self, cell): #clears cell
        cells = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        cellindex = cells.index(cell)
        self.board[cellindex] = " "

    def getopencells(self): #returns open cells
        cells = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        opencells = set()
        for x in range(len(self.board)):
            if self.board[x] == " ":
                opencells.add(x)
        return opencells
    
    def movecausewin(self, cell, sign): #checks if given move causes a win
        self.set(cell, sign)
        if self.isdone():
            self.resetcell(cell)
            return True
        else:
            self.resetcell(cell)
            return False
            
    def isdone(self):  #checks win states, updates winner and done variables accordingly
            done = False
            self.winner = ''
            if self.board[0]==self.board[4]==self.board[8]!=' ':
                done = True
                self.winner = self.board[0]
            elif self.board[2]==self.board[4]==self.board[6]!=' ':
                done = True
                self.winner = self.board[2]
            elif self.board[0]==self.board[1]==self.board[2]!=' ':
                done = True
                self.winner = self.board[0]
            elif self.board[3]==self.board[4]==self.board[5]!=' ':
                done = True
                self.winner = self.board[3]
            elif self.board[6]==self.board[7]==self.board[8]!=' ':
                done = True
                self.winner = self.board[6]
            elif self.board[0]==self.board[3]==self.board[6]!=' ':
                done = True
                self.winner = self.board[0]
            elif self.board[1]==self.board[4]==self.board[7]!=' ':
                done = True
                self.winner = self.board[1]
            elif self.board[2]==self.board[5]==self.board[8]!=' ':
                done = True
                self.winner = self.board[2]
            elif " " not in self.board:
                done = True
                self.winner = "TIE"        

            return done
    
    def show(self): #prints the board
        print("   A   B   C ")
        print(" +---+---+---+")
        print(f"1| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
        print(" +---+---+---+")
        print(f"2| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
        print(" +---+---+---+")
        print(f"3| {self.board[6]} | {self.board[7]} | {self.board[8]} |")
        print(" +---+---+---+")