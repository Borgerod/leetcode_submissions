'''
	You are given an array prices where prices[i] is the price of a given stock on the ith day.

	You want to maximize your profit by choosing a single day to buy 
	one stock and choosing a different day in the future to sell that stock.

	Return the maximum profit you can achieve from this transaction. 
	If you cannot achieve any profit, return 0.
'''

class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		e = concurrent.futures.ThreadPoolExecutor()
		for max_profit in e.map(self.getSolution,  prices):
			if max_profit>0:
				return max_profit
			else: 
				return 0  
	def getSolution(self, prices):
		prices = np.array(prices)
		print(prices)
		ppd = self.makeDict(prices)
		min_ranged = np.array(self.getMinRanged(prices))
		pos = np.array(self.getBuyPos(min_ranged, ppd))
		profit_dict = self.getProfitDict(prices, ppd, min_ranged, pos)
		max_profit = self.getMaxProfit(profit_dict)
		return max_profit



	def makeDict(self, prices):
		ppd = {}
		for i, p in enumerate(prices):
			ppd[i]=p
		return ppd

	def getMinRanged(self, prices):
		return sorted(prices)

	def getBuyPos(self, min_ranged, ppd):
		pos = []
		for i in min_ranged:
			x = list(ppd.keys())[list(ppd.values()).index(i)]
			pos.append(x)
		return pos

	def getMaxPrice(self, x, i):
		return max(x)

	def getSellPos(self, ppd, max_price):
		return list(ppd.keys())[list(ppd.values()).index(max_price)]

	def getProfitDict(self, prices, ppd, min_ranged, pos):
		profit_dict = {}
		for i, m in zip(pos, min_ranged):
			x = prices[i+1:]
			if x.size != 0: 
				max_price = self.getMaxPrice(x, i)
				sell = self.getSellPos(ppd, max_price)
				profit_dict[max_price - m] = [m, sell]
		return profit_dict

	def getMaxProfit(self, profit_dict):
		try:
			return max([i for i in profit_dict])
		except ValueError:
			return 0

'''
	* Ett bedre svar alternativ
'''

# class Solution:
# 	def maxProfit(self,prices):
# 		left = 0 #Buy
# 		right = 1 #Sell
# 		max_profit = 0
# 		while right < len(prices):
# 			currentProfit = prices[right] - prices[left] #our current Profit
# 			if prices[left] < prices[right]:
# 				max_profit =max(currentProfit,max_profit)
# 			else:
# 				left = right
# 			right += 1
# 		return max_profit


# class Input:
# 	def getInput(self) -> list[int]:
# 		# return [7,1,5,3,6,4]
# 		return [7,6,4,3,1]

# 		# return [1,2]
# 		# 
# 		# return [2,7,1,4]



# def main():
# 	I = Input()
# 	s = Solution()
# 	result = s.maxProfit(I.getInput())
# 	print("===")
# 	print(result)

# if __name__ == '__main__':
# 	main()

