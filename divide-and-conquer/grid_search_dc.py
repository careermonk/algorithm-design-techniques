def grid_search(matrix, value, min_row, max_row, min_column, max_column):
	if (min_row == max_row and min_column == max_column and matrix[min_row][min_column] != value):
		return None, None 
	if (matrix[min_row][min_column] > value):
		return None, None 
	if (matrix[max_row][max_column] < value):
		return None, None  
	row_mid = (min_row + max_row) / 2
	column_mid = (min_column + max_column) / 2
	if (matrix[row_mid][column_mid] == value):
		return row_mid, column_mid
	elif (matrix[row_mid][column_mid] < value):
		row, column = grid_search(matrix, value, min_row, row_mid, column_mid + 1, max_column)
		if row is not None and column is not None:
			return row, column
		return grid_search(matrix, value, row_mid + 1, max_row, min_column, max_column)
	else:
		row, column = grid_search(matrix, value, min_row, row_mid - 1, min_column, max_column)
		if row is not None and column is not None:
			return row, column
		return grid_search(matrix, value, row_mid + 1, max_row, min_column, column_mid)

matrix = [[1, 2, 2, 2, 3, 4], 
		[1, 2, 3, 3, 4, 5],
		[3, 4, 4, 4, 4, 6],	
		[4, 5, 6, 7, 8, 9]
		]
print grid_search(matrix, 3, 0, len(matrix)-1, 0, len(matrix[0])-1)
print grid_search(matrix, 2, 0, len(matrix)-1, 0, len(matrix[0])-1)
print grid_search(matrix, 6, 0, len(matrix)-1, 0, len(matrix[0])-1)
