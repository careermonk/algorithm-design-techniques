def arrange_service_requests( A ):
    # sort the service requests based on their service times
    A.sort()

def waiting_time_of_service_request(A, request_number):
    if request_number <= 0 or request_number >= len(A):
        return -1
    return sum(A[:request_number-1])

# array of requests with their service times 
A = [3, 16, 9, 3, 5, 1, 4 , 7, 19]
arrange_service_requests(A)

waiting_time = waiting_time_of_service_request(A, 3)
print waiting_time

waiting_time = waiting_time_of_service_request(A, 7)
print waiting_time
