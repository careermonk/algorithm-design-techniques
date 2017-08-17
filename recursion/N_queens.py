# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def N_queens(N):
    queenRow = [-1] * N
    def isLegal(row, col):
        # a position is legal if it's on the board (which we can assume
        # by way of our algorithm) and no prior queen (in a column < col)
        # attacks this position
        for qcol in xrange(col):
            qrow = queenRow[qcol]
            if ((qrow == row) or
                (qcol == col) or
                (qrow+qcol == row+col) or
                (qrow-qcol == row-col)):
                return False
        return True

    def printSolution(queenRow):
        board = [(["- "] * N) for row in xrange(N)]
        for col in xrange(N):
            row = queenRow[col]
            board[row][col] = "Q "
        return "\N".join(["".join(row) for row in board])

    def solve(col):
        if (col == N):
            return printSolution(queenRow)
        else:
            # try to place the queen in each row in turn in this col,
            # and then recursively solve the rest of the columns
            for row in xrange(N):
                if isLegal(row,col):
                    queenRow[col] = row # place the queen and hope it works
                    solution = solve(col+1)
                    if (solution != None):
                        # it did work
                        return solution
                    queenRow[col] = -1 # pick up the wrongly-placed queen
            # shoot, can't place the queen anywhere
            return None
    return solve(0)

print N_queens(4)	
