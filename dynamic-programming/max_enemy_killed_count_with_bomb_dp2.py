# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def max_enemy_killed_count_with_bomb(matrix2d):
        if not matrix2d or not matrix2d[0]:
            return 0

        wall  = 'W'
        enemy = 'E'
        empty = '0'

        n = len(matrix2d)
        m = len(matrix2d[0])

        # for each empty cell, how many enemies in the same row will be killed if bomb there
        row_kill_counts = [ [ 0 for j in range(m) ] for i in range(n) ]

        # for each empty cell, how many enemies in the same col will be killed if bomb there
        col_kill_counts = [ [ 0 for j in range(m) ] for i in range(n) ]

        # calculate row_kill_counts
        for i in range(n):
            empty_cols = []
            kill_count = 0

            for j in range(m+1):
                if j==m or matrix2d[i][j] == wall:
                    for emptyCol in empty_cols:
                        row_kill_counts[i][emptyCol] = kill_count
                    kill_count = 0
                    empty_cols = []
                elif matrix2d[i][j] == enemy:
                    kill_count += 1
                elif matrix2d[i][j] == empty:
                    empty_cols.append( j )

        # calculate col_kill_counts
        for j in range(m):
            empty_rows = []
            kill_count = 0

            for i in range(n + 1):
                if i == n or matrix2d[i][j] == wall:
                    for emptyRow in empty_rows:
                        col_kill_counts[emptyRow][j] = kill_count
                    kill_count = 0
                    empty_rows = []
                elif matrix2d[i][j] == enemy:
                    kill_count += 1
                elif matrix2d[i][j] == empty:
                    empty_rows.append(i)

        # find max of row_kill_counts and col_kill_counts
        ret = 0
        for i in range(n):
            for j in range(m):
                ret = max( ret, row_kill_counts[i][j] + col_kill_counts[i][j] )
        return ret

print max_enemy_killed_count_with_bomb([['0','E','0','0'],['E','0','W','E'],[0,'E','0','0']])
