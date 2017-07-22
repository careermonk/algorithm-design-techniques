def grid_search(matrix, value):
	m = len(matrix)
	if m == 0:
		return None, None

	n = len(matrix[0])
	if n == 0:
		return None, None

	i = 0
	j = n - 1

	while i < m and j >= 0:
		if matrix[i][j] == value:
			return i, j
		elif matrix[i][j] < value:
			i = i + 1
		else:
			j = j - 1

	return None, None

matrix = [[1, 2, 2, 2, 3, 4], 
		[1, 2, 3, 3, 4, 5],
		[3, 4, 4, 4, 4, 6],	
		[4, 5, 6, 7, 8, 9]
		]

print grid_search(matrix, 3)
print grid_search(matrix, 2)
print grid_search(matrix, 6)
