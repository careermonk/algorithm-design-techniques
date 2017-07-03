def number_of_platforms_required(arrivals, departures):
    arrivals.sort()
    departures.sort()
    i = 0
    j = 0
    max_overlapped_intervals = 0 
    number_of_overlaps = 0
    while (i < len(arrivals) and j < len(departures)):
        if arrivals[i] < departures[j]:
            i += 1
            number_of_overlaps += 1
            if number_of_overlaps > max_overlapped_intervals:
                max_overlapped_intervals = number_of_overlaps
        else:
            number_of_overlaps -= 1
            j += 1

    return max_overlapped_intervals

# array of train arrivals and departures
arrivals = [900, 915, 1030, 1045]
departures = [930, 1300, 1100, 1145]
number_of_platforms = number_of_platforms_required(arrivals, departures)
print number_of_platforms
