class Tic_Tac_Toe():
    def __init__(self):
        pass

    def row_check(self, board):

        for b in range(len(board)):
            if board[b] == "_":
                continue
            if b % 3 == 0:
                if board[b] == board[b + 1] == board[b + 2]:
                    return True
        return False


    def col_check(self, board):
        for b in range(len(board)):
            if board[b] == "_":
                continue
            if b - 3:
                if board[b] == board[b + 3] == board[b + 6]:
                    return True
        return False


    def row_stop_win_check(self, board):
        row0 = board[0:3]
        row1 = board[3:6]
        row2 = board[6:9]

        def check_row(row):
            counter = 0
            for r in range(len(row)):
                if row[r] == "X":
                    counter +=1
            if counter == 2:
                try:
                    return row.index('_')
                except Exception as e:
                    return -1 

            return -1

        if check_row(row0) != -1:
            return check_row(row0)

        if check_row(row1) != -1:
            return check_row(row1) + 3

        if check_row(row2) != -1:
            return check_row(row2) + 6

        return -1
