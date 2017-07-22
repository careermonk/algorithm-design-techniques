def grid_search(matrix, value):
	m = len(matrix)
	n = len(matrix[0])
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == value:
				return i, j

	return None, None

matrix = [[1, 2, 2, 2, 3, 4], 
		[1, 2, 3, 3, 4, 5],
		[3, 4, 4, 4, 4, 6],	
		[4, 5, 6, 7, 8, 9]
		]

print grid_search(matrix, 3)
print grid_search(matrix, 2)
print grid_search(matrix, 6)
