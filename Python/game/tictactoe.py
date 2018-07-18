class Board():
    def __init__(self):
        self._rows = 3
        self._cols = 3
        self._board = [ ['-' for y in range(self._rows)] for x in range(self._cols) ]
        self._current_move = "HUMAN" # HUMAN or AI

    def add_token(self, token, row, col):
        # Assume all params good
        assert(self._board[row][col] == '-')
        self._board[row][col] = token

    def print_board(self):
        for row in range(self._rows):
            rep = ''
            for col in range(self._cols):
                rep += self._board[row][col]
                if col <= 1:
                    rep += '|'
            print(rep)
    
    def is_board_full(self):
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] == '-':
                    return False
        # Board is full here.
        return True

    # Computer is always 'O'
    def ai_make_move(self):
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] == '-':
                    self._board[row][col] = 'O'
                    return
        raise RuntimeError("No valid move for me.")

    def check_move_is_valid(self, row, col):
        # Check to see row and col are valid values
        if (row < 0) or (row > 2):
            return False
        if (col < 0) or (col > 2):
            return False
        # Check to see cell is empty
        return self._board[row][col] == '-'

    def game_loop(self):
        # Human always first:
        while not self.is_board_full():
            print("-----------------------------------------------------------------------")
            self.print_board()
            if self._current_move == "HUMAN":
                move = input("Enter row col:")
                while True:
                    row_str, col_str = move.split(" ")
                    try:
                        row = int(row_str)
                        col = int(col_str)
                    except:
                        print("Invalid input. Try again.")
                        continue
                    if self.check_move_is_valid(row, col):
                        self._board[row][col] = 'X'
                        self._current_move = "AI"
                        break
                    print("Invalid input. Try again.")
                    move = input("Enter row col:")
                    # continues
            elif self._current_move == "AI":
                self.ai_make_move()
                self._current_move = "HUMAN"
            else:
                assert(False)



board = Board()
board.game_loop()
