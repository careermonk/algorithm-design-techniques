from operator import itemgetter
from math import sqrt, pow
def distance(a, b):
	return sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2))

def closest_points_2d(points):
	minimum = float("infinity")
	for i in range(0, len(points)-1):
		for j in range(i+1, len(points)):
			d = distance(points[i], points[j])
			if d < minimum:
				minimum = d
				x = i
				y = j
		return points[x], points[y]

A = [[12,30], [40, 50], [5, 1], [12, 10], [3,4]]
first_point, second_point = closest_points_2d(A)
print "Closest pair is:", first_point, second_point, "and the distance is", distance(first_point, second_point)
