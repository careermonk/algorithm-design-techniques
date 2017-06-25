def max_enemy_killed_count_with_bomb(matrix2d):
        if not matrix2d or not matrix2d[0]:
            return 0
	
	wall  = 'W'
	enemy = 'E'
	empty = '0'
	
	n = len(matrix2d)
	m = len(matrix2d[0])
	max_killed_count = 0
    
	for i in range(n):
		for j in range(m):
            
			if matrix2d[i][j] == empty:
				count = 0

				#count all possible kills in its upward direction
				k = i-1
				while (k >= 0):
					if matrix2d[k][j] == enemy:
						count =  count + 1
					elif matrix2d[k][j] == wall:
						break
					k = k-1

				#count all possible kills in its downward direction
				k = i+1
				while (k < n):
					if matrix2d[k][j] == enemy:
						count =  count + 1
					elif matrix2d[k][j] == wall:
						break
					k = k+1

				#count all possible kills in its right direction
				k = j+1
				while (k < m):
					if matrix2d[i][k] == enemy:
						count =  count + 1
					elif matrix2d[i][k] == wall:
						break
					k = k+1

				#count all possible kills in its left direction
				k = j-1
				while (k >= 0):
					if matrix2d[i][k] == enemy:
						count =  count + 1
					elif matrix2d[i][k] == wall:
						break
					k = k-1
                
		if max_killed_count < count:
			max_killed_count = count

	return max_killed_count

print max_enemy_killed_count_with_bomb([['0','E','0','0'],['E','0','W','E'],[0,'E','0','0']])
