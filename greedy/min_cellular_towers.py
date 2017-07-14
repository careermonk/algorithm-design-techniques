def min_cellular_towers(houseLocations, cellTowerCoverage):
#Sort the house locations in increasing order, removing any duplicates.
	if len(houseLocations) == 0:
		return 0, []


	houseLocations.sort()
	towerLocations = []

	#First tower is as far down the road as possible.
	indexofLastTower = 0
	tower =  houseLocations[0] + cellTowerCoverage 
	towerLocations.append(tower)

	for i in range(1,  len(houseLocations)):
		if abs(houseLocations[i] - tower) > cellTowerCoverage:
			indexofLastTower += 1
			tower =  houseLocations[i] + cellTowerCoverage 
			towerLocations.append(tower)
	return len(towerLocations), towerLocations

# Test Cases
print "Minimum refills required for reaching destination:", min_cellular_towers([50, 10, 14, 3, 5, 8, 21, 37, 55, 44, 59, 39, 75, 66, 19, 29, 88, 80, 63, 69, 31, 25], 9)
