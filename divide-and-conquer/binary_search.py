#Iterative Binary Search Algorithm
def binary_search_iterative(numbersList, value):
    low = 0
    high = len(numbersList)-1
    while low <= high: 
        mid = (low+high)//2
        if numbersList[mid] > value: high = mid-1
        elif numbersList[mid] < value: low = mid+1
        else: return mid
    return -1
	
A = [534,246,933,127,277,321,454,565,220]
print(binary_search_iterative(A,277))

#Recursive Binary Search Algorithm
def binary_search_recursive(numbersList, value, low = 0, high = -1):
    if not numbersList: return -1
    if(high == -1): high = len(numbersList)-1
    if low == high:
        if numbersList[low] == value: return low
        else: return -1
    mid = low + (high-low)//2
    if numbersList[mid] > value: 
        return binary_search_recursive(numbersList, value, low, mid-1)
    elif numbersList[mid] < value: 
        return binary_search_recursive(numbersList, value, mid+1, high)
    else: return mid
	    
A = [534,246,933,127,277,321,454,565,220]
print(binary_search_recursive(A,277))  
