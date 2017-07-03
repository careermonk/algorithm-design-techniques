def number_of_platforms_required(arrivals, departures):
    
    arrivals.sort()
    departures.sort()
    i = 0
    j = 0
    merged_list = []
    while (i < len(arrivals) and j < len(departures)):
        if arrivals[i] < departures[j]:
            merged_list.append('A')
            i += 1
        else:
            merged_list.append('D')
            j += 1
    
    while (i < len(arrivals)):
        merged_list.append('A')
        i += 1
    
    while (j < len(departures)):
        merged_list.append('D')
        j += 1

    print merged_list
    max_overlapped_intervals = 0 
    number_of_overlaps = 0
    for i in range(len(merged_list)):  
        if merged_list[i] == 'A':
            number_of_overlaps += 1
        else:
            number_of_overlaps -= 1

        if number_of_overlaps > max_overlapped_intervals:
            max_overlapped_intervals = number_of_overlaps
    
    return max_overlapped_intervals

# array of train arrivals and departures
arrivals = [900, 915, 1030, 1045]
departures = [930, 1300, 1100, 1145]
number_of_platforms = number_of_platforms_required(arrivals, departures)
print number_of_platforms
