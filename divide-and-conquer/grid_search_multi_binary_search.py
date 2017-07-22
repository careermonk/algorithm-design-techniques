def binary_search(A, value):
    low = 0
    high = len(A)-1
    while low <= high: 
        mid = (low+high)//2
        if A[mid] > value: high = mid-1
        elif A[mid] < value: low = mid+1
        else: return mid, mid
    return low, high

def grid_search(matrix, value, min_row, max_row, min_column, max_column):
	if (min_row == max_row and min_column == max_column \
				and matrix[min_row][min_column] != value):
		return None, None 
	if (matrix[min_row][min_column] > value):
		return None, None 
	if (matrix[max_row][max_column] < value):
		return None, None  
	row_mid = (min_row + max_row) / 2
	bs_left, bs_right = binary_search(matrix[row_mid],value)
	if bs_left == bs_right:
		return row_mid, bs_right
	else:
		row, column = grid_search(matrix, value, row_mid+1, max_row, min_column, bs_left-1)
		if row is not None and column is not None:
			return row, column
		return grid_search(matrix, value, min_row, row_mid-1, bs_right+1, max_column)

matrix = [[1, 2, 2, 2, 3, 4], 
		[1, 2, 3, 3, 4, 5],
		[3, 4, 4, 4, 4, 6],	
		[4, 5, 6, 7, 8, 9]
		]
print grid_search(matrix, 6, 0, len(matrix)-1, 0, len(matrix[0])-1)
print grid_search(matrix, 2, 0, len(matrix)-1, 0, len(matrix[0])-1)
print grid_search(matrix, 3, 0, len(matrix)-1, 0, len(matrix[0])-1)
