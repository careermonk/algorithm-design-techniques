from operator import itemgetter
def closest_points_1d(points):
	# if points have same y values
	if points[0][1] == points[1][1]:
		points.sort(key=itemgetter(0), reverse=False)
		min = float("infinity")
		x = float("infinity")
		for i in range(1, len(points)-1):
			if min > points[i][0]-points[i-1][0]:
				min = points[i][0]-points[i-1][0]
				x = i
		return points[x], points[x-1]
	else:
		points.sort(key=itemgetter(1), reverse=False)
		min = float("infinity")
		y = float("infinity")
		for i in range(1, len(points)-1):
			if min > points[i][1]-points[i-1][1]:
				min = points[i][1]-points[i-1][1]
				y = i
		return points[y], points[y-1]

A = [[2,2], [7,2], [5,2], [4,2], [9,2], [11,2]]
print closest_points_1d(A)

A = [[2,2], [2,7], [2,5], [2,4], [2,9], [2,11]]
print closest_points_1d(A)
