
N = 9

def isSafe(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i]==num:
            return False
        
    for i in range(9):
        if sudoku[i][col]==num:
            return False
        
    startRow=row-row%3
    startCol=col-col%3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow+i][startCol+j]==num:
                return False
    return True

def solveSudoku(sudoku, row, col):
    # If reached past last row, puzzle solved
    if row == N:
        return True

    # Move to next row if past last column
    if col == N:
        return solveSudoku(sudoku, row + 1, 0)

    # Skip pre-filled cells
    if sudoku[row][col] > 0:
        return solveSudoku(sudoku, row, col + 1)

    for num in range(1, N + 1):
        if isSafe(sudoku, row, col, num):
            sudoku[row][col] = num
            if solveSudoku(sudoku, row, col + 1):
                return True
            sudoku[row][col] = 0
    return False

def isValidSudoku(board):
    for i in range(9):
        # create empty dictionaries to keep track of row, column, and block values
        row = {}
        column = {}
        block = {}
        # calculate the starting index of the current 3x3 block
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
            # check if the value in the current cell of the row is valid
            if board[i][j]!=0 and board[i][j] in row:
                return False
            row[board[i][j]] = 1  # add the value to the row dictionary
            
            # check if the value in the current cell of the column is valid
            if board[j][i]!=0 and board[j][i] in column:
                return False
            column[board[j][i]] = 1  # add the value to the column dictionary
            
            # calculate the row and column index of the current cell within the 3x3 block
            rc = row_cube+j//3
            cc = column_cube + j%3
            
            # check if the value in the current cell of the block is valid
            if board[rc][cc] in block and board[rc][cc]!=0:
                return False
            block[board[rc][cc]] = 1  # add the value to the block dictionary
    return True

def solver(sudoku):
    if isValidSudoku(sudoku):
        solveSudoku(sudoku,0,0)
        return sudoku
    else:
        return "no"