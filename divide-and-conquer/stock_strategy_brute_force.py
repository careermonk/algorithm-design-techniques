# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

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
