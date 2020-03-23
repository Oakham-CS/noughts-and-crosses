# Baker, Bell, Boshoff, Dowell, Farzulla
# Noughts and Crosses - GitHub
# 23/03/2020
# v 0.1

class Board:
    # TODO HARRY
    # Please add in-line comments describing this class and it's properties/functions

    def __init__(self, w, h):
        self.width, self.height = w, h

    def displayBoard(self):        
        pass

    def clearBoard(self):
        pass


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

    board = Board(3, 3)
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
    
    
    


