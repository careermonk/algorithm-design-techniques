def paint_house_k_colors_dp(costs):
    n = len(costs)
    k = len(costs[0])
    if n < 1:
        return None
    elif n == 1:
        return min(costs[0])

    C = [[float("inf") for j in range(k)] for i in range(n)]
    C[0] = costs[0]
    print C
    # calculate mininum cost to paint n houses
    for i in range(1, n):
    	for j in range(0, k):
            for m in range(0, k):
                if m != j:
                        C[i][j] = min(C[i-1][m] + costs[i][j], C[i][j])

    return min(C[n - 1])

print paint_house_k_colors_dp([[13,	2,	10], [10,	13, 	5], [13,	4,	9]])
