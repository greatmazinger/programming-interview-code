"""
Minesweeper for the the console.

Author: Raoul Veroy
"""

from enum import Enum

class State(Enum):
    SPACE = 1
    MINE = 2
    HIDDEN_SPACE = 3
    HIDDEN_MINE = 4

# Board class for the game
class Board:
    def __init__( self, width = 9, height = 9, num_mines = 10 ):
        """Create a Minesweeper board. Default size is 9x9."""
        if num_mines >= (height * width):
            raise ValueError("More mines than there are cells on the board!")
        self._board = [ [ State.HIDDEN_SPACE for y in range(width) ] for x in range(height) ]
        self._height = height
        self._width = width
        self._num_mines = num_mines

    @property
    def height( self ):
        return self._height

    @property
    def width( self ):
        return self._width

    def _print_status( self ):
        """Print status of the game for debugging."""
        print("Minesweeper:")
        print("Board: %d x %d" % (self._width, self._height))

    def print_board( self ):
        board = self._board
        for x in range(self._width):
            row = ''
            for y in range(self._height):
                if board[x][y] == State.SPACE:
                    row = ''.join([ row, "_ " ])
                elif ( (board[x][y] == State.HIDDEN_MINE) or
                       (board[x][y] == State.HIDDEN_SPACE) ):
                    row = ''.join([ row, "? " ])
                else:
                    print("DEBUG: [%d][%y] = %s" % (x, y, str(board[x][y])))
                    raise RuntimeError("Invalid board state: exposed mine should have ended the game.")
            print(row)
