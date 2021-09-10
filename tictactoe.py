# tictactoe version 2
# not sure what happened to version 1 but this is version 2
# <10-sep-2021>

# board class
# keeps track of the "board" (a 3 by 3 array)
# have methods that will be able to update board and get board
class board:
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

    # returns the board
    def getBoard(self):
        return self.board

    # for updating the board
    def updateBoard(self, position):
        row = (position-1)/3
        col = (position-1) % 3
        self.board[row][col] = 'm'


class game:
    # creating a new board to start the game
    board = board()
