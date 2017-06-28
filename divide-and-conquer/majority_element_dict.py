def majority_element(A):
	dict = {}

	for i in A:
		dict[i] = dict.get(i, 0) + 1
		if dict[i] > len(A)/2:
			return i

	return None

A = [1, 2, 3, 4, 3, 3, 3, 3, 3, 2, 2, 3, 7, 3, 3, 3]
print majority_element(A)
