def number_of_platforms_required(arrivals, departures):
    max_overlapped_intervals = 0 
    
    for i in range(len(arrivals)):  # or for i in range(len(departures)) 
        number_of_overlaps = 1
        for j in range(i+1, len(arrivals)):
            if arrivals[j] >= arrivals[i] and arrivals[j] < departures[i]:
                number_of_overlaps += 1
    
        if number_of_overlaps > max_overlapped_intervals:
            max_overlapped_intervals = number_of_overlaps
    
    return max_overlapped_intervals

# array of train arrivals and departures
arrivals = [900, 915, 1030, 1045]
departures = [930, 1300, 1100, 1145]
number_of_platforms = number_of_platforms_required(arrivals, departures)
print number_of_platforms
