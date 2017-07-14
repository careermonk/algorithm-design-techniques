def fractional_knapsack(weights, values, C):
  "Given problem (weights, values, C), return best fractional_knapsack solution"
  n = len(weights)
  assert n==len(values)
  x = [0]*n
  totalProfit = 0
  # Idea: take highest profit items first, only last item taken may be fractional_knapsack.
  used = 0
  for profit, i in sorted([(float(values[i])/weights[i], i) for i in range(n)], reverse=True):
    if used+weights[i] <= C:
      used += weights[i]
      x[i] = 1
      totalProfit += profit
    else:
      x[i] = float(C-used)/weights[i]
      totalProfit += x[i]*values[i]
      # remainder of x remains 0
      break

  return x, totalProfit

weights = [1, 5, 3, 3]
values = [10, 35, 18, 12]
selectedItems, profit = fractional_knapsack(weights, values, 8)
print "Selected items:", selectedItems, "with profit",profit
