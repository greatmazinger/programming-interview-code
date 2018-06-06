import fileinput

def new_square_filled_with_zeroes(size = 1):
    if size == 1:
        return [ [0] ]
    else:
        return [ [0 for row in xrange(0, size)] for col in xrange(0, size) ]

def test_fill( square = [], size = 0 ):
    val = 1
    for row in xrange(0, size):
        for col in xrange(0, size):
            square[row][col] = val
            val += 1

def fill_base_case_even( square = [],
                         row_start = 0,
                         col_start = 0,
                         base = 0 ):
    # Base case even is 2x2
    # (0,0) is the start
    square[0 + row_start][0 + col_start] = current = base + 1
    square[0 + row_start][1 + col_start] = current = current + 1
    square[1 + row_start][1 + col_start] = current = current + 1
    square[1 + row_start][0 + col_start] = current = current + 1
    return current
    
def fill_spiral( square = [],
                 row_start = 0,
                 col_start = 0,
                 size = 0,
                 base = 0 ):
    if size <= 0:
        return base 
    # Go around the edges. There are 4:
    # Going in this order - top, right, bottom, left
    current = base
    row = row_start
    col = col_start
    for edge in ["top", "right", "bottom", "left"]:
        for elem in xrange(0, size - 1):
            square[row][col] = current = current + 1
            if edge == "top":
                col += 1
            elif edge == "right":
                row += 1
            elif edge == "bottom":
                col -= 1
            elif edge == "left":
                row -= 1
    if size == 1:
        # Base case odd is a 1x1 square
        square[row_start][col_start] = largest = base + 1
    elif size == 2:
        # Base case even
        largest = fill_base_case_even( square = square,
                                       row_start = row_start,
                                       col_start = col_start,
                                       base = base )
    else:
        # Even
        largest = fill_spiral( square = square,
                               row_start = row_start + 1,
                               col_start = col_start + 1,
                               size = size - 2,
                               base = current )

    return largest

def print_square(square = [], size = 0):
    for row in xrange(0, size):
        for col in xrange(0, size):
            print square[row][col],
        print

if __name__ == "__main__":
    stdin = fileinput.input()
    num = int(stdin.next())
    print "--------------------------------------------------------------------------------"
    square = new_square_filled_with_zeroes(num)
    fill_spiral( square,
                 row_start = 0,
                 col_start = 0,
                 size = num,
                 base = 0 )
    print_square(square, size = num)
