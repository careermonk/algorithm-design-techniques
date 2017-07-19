import math
def two_eggs(floors):
	t1 = math.sqrt((1^2) + (4*1*200))
	t3 = (-1 + t1)/2
	t4 = (-1 - t1)/2
	return math.ceil(max(t3,t4))

floors = 100
eggs = 2
print("Minimum attempts in worst case with %d eggs from %d floors = %d" % (eggs,floors,two_eggs(floors)))
