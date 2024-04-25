def is_solved_row(board: list[list[int]], row: int, figure: int) -> bool:
    return all(element == figure for element in board[row])
    
def is_solved_all_rows(board: list[list[int]], figure: int) -> bool:
    return any(is_solved_row(board, row, figure) for row in range(len(board)))

def is_solved_column(board: list[list[int]], column: int, figure: int) -> bool:
    return all(element == figure for element in [row[column] for row in board])

def is_solved_all_columns(board: list[list[int]], figure: int) -> bool:
    return any(is_solved_column(board, column, figure) for column in range(len(board[0])))

def is_solved_diagonal(board: list[list[int]], figure: int) -> bool:
    if (board[0][0] == figure and board[1][1] == figure and board[2][2] == figure) \
    or (board[2][0] == figure and board[1][1] == figure and board[0][2] == figure):
        return True
    else: 
        return False

def is_empty_spaces(board: list[list[int]]) -> bool:
    return any(0 in element for element in board)

def is_solved(board: list[list[int]]) -> int:
    cross: int = 1
    zero: int = 2
    if is_solved_all_rows(board=board, figure=cross) \
        or is_solved_all_columns(board=board, figure=cross) \
        or is_solved_diagonal(board=board, figure=cross):
        return cross
    elif is_solved_all_rows(board=board, figure=zero) \
        or is_solved_all_columns(board=board, figure=zero) \
        or is_solved_diagonal(board=board, figure=zero):
        return zero
    elif is_empty_spaces(board=board):
        return -1
    else:
        return 0
    

    
board: list[list[int]] = [
         [0, 1, 1],
         [0, 1, 2],
         [1, 1, 1]
]
print(is_solved(board))
