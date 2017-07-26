def get_change(amount):
	"""Changing money optimally.
	"""
	coins = [100, 1, 25, 5, 50, 10]  # must be sorted
	coins.sort(reverse=True)
	count = 0
	selectedCoins = []
	for coin in coins:
		# Update count with the the number of coins 'are held' in the amount.
		if amount < coin:
			continue
		count += amount // coin
		selectedCoins.append(coin * (amount // coin))
		# Put remainder to the residuary amount.
		amount %= coin

	return count, selectedCoins

if __name__ == "__main__":
	n = 37
	print(get_change(n))
