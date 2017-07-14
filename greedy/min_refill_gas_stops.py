def min_refill_gas_stops(stationDist, carMaxDistance):
    curPos = 0
    minRefill = 0
    curDistance = carMaxDistance
    numRefillStations = len(stationDist)
    
    while(curPos<numRefillStations):
        while(curPos < numRefillStations and stationDist[curPos] <= curDistance):
            curPos += 1

        if (curPos >= numRefillStations):
            return minRefill

        curPos -= 1
        minRefill += 1
        curDistance = stationDist[curPos] + carMaxDistance
     

    if (stationDist[curPos] < curDistance):
        minRefill += 1
    
    return minRefill
   

# Test Cases
print "Minimum refills required for reaching destination:", min_refill_gas_stops([0, 20, 37, 55, 75, 95], 40)
