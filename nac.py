# Baker, Bell, Boshoff, Dowell, Farzulla
# Noughts and Crosses - GitHub
# 23/03/2020
# v 0.1

class Board:
    # TODO HARRY
    # Please add in-line comments describing this class and it's properties/functions

    def __init__(self):
        self.width, self.height = 3, 3
        self.grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


    def displayBoard(self):        
        print(self.grid[0], "|", self.grid[1], "|", self.grid[2])
        print("---------")
        print(self.grid[3], "|", self.grid[4], "|", self.grid[5])
        print("---------")
        print(self.grid[6], "|", self.grid[7], "|", self.grid[8])
        print ("\n ============================================================================")


    def setGrid(self, counter, index):
        self.grid[index] = counter
    def getGrid(self, index):
        return(self.grid[index])
        
    def clearBoard(self):
        #reset grid
        self.grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Game:
    # TODO MURAD

    def __init__(self, a, b, board):
        self.playerA = a
        self.playerB = b
        self.board = board

    def newGame(self):
        pass

    def checkWinner(self):
        # TODO Alex Bell
        # return A, B or DRAW
        pass

class Player:
    # TODO ALEX DOWELL

    def __init__(self, name, counter):
        self.name = name
        self.counter = counter

    def playCounter(self, position):
        # position comes in as 1..9 (top left, across in rows)
        pass
        

# some test code...

if __name__ == "__main__":
  
    board = Board()
    board.displayBoard()

    susan = Player('Susan','X')
    bob = Player('Bob','O')
    game = Game(bob, susan, board) 

    game.board.clearBoard()
    susan.playCounter(1)
    game.board.displayBoard()
    game.checkWinner()
    bob.playCounter(5)
    game.board.displayBoard()
    game.checkWinner()
    
    
    


