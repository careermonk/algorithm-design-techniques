def min_refill_gas_stops(stationDist, maxDistance):
    curPos = 0
    minRefill = 0
    curDistance = maxDistance
    numRefillStations = len(stationDist)
    stops = []
    while(curPos<numRefillStations):
        while(curPos < numRefillStations and stationDist[curPos] <= curDistance):
            curPos += 1

        if (curPos >= numRefillStations):
            return minRefill, stops

        curPos -= 1
        minRefill += 1
        curDistance = stationDist[curPos] + maxDistance

        if (stationDist[curPos] < curDistance):
            minRefill += 1
            stops.append(curPos)
    
    return minRefill, stops

# Test Cases
print "Minimum refills required for reaching destination:", min_refill_gas_stops([0, 20, 37, 55, 75, 95], 40)
