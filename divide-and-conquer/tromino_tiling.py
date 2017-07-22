empty_cell = -1

#nextTile is the number of next available tromino tile
#The origin coordinates of the board are given by originR and originC
def recursiveTile(board, size, originR, originC, rMiss, cMiss, nextTile):

    # missing square quadrant number
    quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)
    
    #base case of 2x2 board
    if size == 2: 
        tilePos = [(0,0), (0,1), (1,0), (1,1)]
        tilePos.pop(quadMiss)
        for (r, c) in tilePos:
            board[originR + r][originC + c] = nextTile
        nextTile = nextTile + 1
        return nextTile

    #recurse on each quadrant    
    for quad in range(4):
        shiftR = size//2 * (quad >= 2)
        shiftC = size//2 * (quad % 2 == 1)
        if quad == quadMiss:
            #Pass the new origin and the shifted rMiss and cMiss
            nextTile = recursiveTile(board, size//2, originR + shiftR,\
                originC + shiftC, rMiss - shiftR, cMiss - shiftC, nextTile)

        else:
            #The missing square is different for each of the other 3 quadrants
            newrMiss = (size//2 - 1) * (quad < 2)
            newcMiss = (size//2 - 1) * (quad % 2 == 0)
            nextTile = recursiveTile(board, size//2, originR + shiftR,\
                            originC + shiftC, newrMiss, newcMiss, nextTile)

    #place center tromino
    centerPos = [(r + size//2 - 1, c + size//2 - 1)
                 for (r,c) in [(0,0), (0,1), (1,0), (1,1)]]
    centerPos.pop(quadMiss)
    for (r,c) in centerPos: # assign tile to 3 center squares
        board[originR + r][originC + c] = nextTile
    nextTile = nextTile + 1

    return nextTile

#This procedure is a wrapper for recursiveTile that does all the work
def tromino_tiling(n, rMiss, cMiss):
    #Initialize board, this is the only memory that will be modified!
    board = [[empty_cell for i in range(2**n)] for j in range(2**n)] 
    recursiveTile(board, 2**n, 0, 0, rMiss, cMiss, 0)
    return board

#This procedure prints a given tiled board using letters for tiles
def print_board(board):
    for i in range(len(board)):
        row = ''
        for j in range(len(board[0])):
            if board[i][j] != empty_cell:
                row += chr((board[i][j] % 10) + ord('0')) + ' '
            else:
                row += ' '
        print (row)

print_board(tromino_tiling(3, 4, 6))
