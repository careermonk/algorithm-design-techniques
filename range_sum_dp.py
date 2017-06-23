cumulative_sum = []
def cumulative_sum_pre_process(A):
	global cumulative_sum
	cumulative_sum.append(A[0])
	for i in range(0, len(A)):
		cumulative_sum.append(cumulative_sum[i] + A[i])

def range_sum_dp(A, start_index, end_index):
    return cumulative_sum[end_index+1] - cumulative_sum[start_index]

A= [-2, 1, 6, -5, 9, -1, 19]
cumulative_sum_pre_process(A)
print range_sum_dp(A, 0, 3)
print range_sum_dp(A, 2, 6)
print range_sum_dp(A, 5, 5)
