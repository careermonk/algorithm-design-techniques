def paint_house_min_cost_dp(costs):
    n = len(costs)
    if n < 1:
        return None
    elif n == 1:
        return min(costs[0])

    # calculate mininum cost to paint n houses
    for i in range(1, n):
        costs[i][0] = min(costs[i - 1][1] + costs[i][0], costs[i - 1][2] + costs[i][0])
        costs[i][1] = min(costs[i - 1][0] + costs[i][1], costs[i - 1][2] + costs[i][1])
        costs[i][2] = min(costs[i - 1][0] + costs[i][2], costs[i - 1][1] + costs[i][2])

    return min(costs[n - 1])


print paint_house_min_cost_dp([[13,	2,	10], [10,	13, 	5], [13,	4,	9]])
