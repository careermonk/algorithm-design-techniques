# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

def find_max_crossing_subarray(A, low, mid, high):
    # calculate index boundary and sum of left max sub-A

    left_sum = float("-inf")
    max_left = None
    max_subarray_sum = 0

    for i in range(mid, low - 1, -1):
        max_subarray_sum += A[i]
        if max_subarray_sum > left_sum:
            left_sum = max_subarray_sum
            max_left = i

    # calculate index boundary and sum of right max sub-A
    right_sum = float("-inf")
    max_right = None
    max_subarray_sum = 0

    for i in range(mid + 1, high + 1):
        max_subarray_sum += A[i]
        if max_subarray_sum > right_sum:
            right_sum = max_subarray_sum
            max_right = i

    return max_left, max_right, left_sum + right_sum

def max_contigous_sum_with_divide_and_conquer(A, low, high):
    # base case: one element in A
    if high == low:
        return low, high, A[low]

    # recursive case: >1 element in A
    else:
        mid = (low + high) // 2

        # recursive sub-problems
        left_low, left_high, left_sum = max_contigous_sum_with_divide_and_conquer(A, low, mid)
        right_low, right_high, right_sum = max_contigous_sum_with_divide_and_conquer(A, mid + 1, high)

        # crossing sub-problem
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        # case 1: max subarray is in left A
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        # case 2: max subarray is in right A
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        # case 3: max subarray is in A crossing midpoint
        else:
            return cross_low, cross_high, cross_sum

list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print max_contigous_sum_with_divide_and_conquer(list, 0, len(list) - 1)
