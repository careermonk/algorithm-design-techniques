def calculate_profit_when_buying_now(A, index):
  buyingPrice = A[index]
  maxProfit = 0
  sellAt = index
  for i in range(index+1, len(A)):
      sellingPrice = A[i]
      profit = sellingPrice - buyingPrice
      if profit > maxProfit:
	  maxProfit = profit
	  sellAt = i

  return maxProfit, sellAt
  
# check all possible buying times
def stock_strategy_brute_force(A):
  maxProfit = 0
  buy = None
  sell = None
  
  for index, item in enumerate(A):
      profit, sellAt = calculate_profit_when_buying_now(A, index)
      if (maxProfit is None) or (profit > maxProfit):
	  maxProfit = profit
	  buy = index
	  sell = sellAt
	  
  return maxProfit, buy, sell

A=[7, 1, 5, 3, 6, 4]
print stock_strategy_brute_force(A)
