class Solution:
	def __init__(self) -> None:
		self.price_list = []
		self.max_price = 0
		self.min_price = 0
		self.result = 0

	def setMin(self):
		if self.price_list:
			self.min_price = min(self.price_list)
		else:
			self.min_price = 0

	def setMax(self):
		if self.price_list:
			self.max_price = max(self.price_list)
		else:
			self.max_price = 0

	def checkIfTrue(self):
		# Only valid if min and max are actually in the list
		if self.max_price in self.price_list and self.min_price in self.price_list:
			return self.price_list.index(self.max_price) > self.price_list.index(self.min_price)
		return False

	def maxProfit(self, prices: list[int]) -> int:
		result = 0 #default val
		if len(prices) < 2:  # edge case
			return result

		self.price_list = prices
		self.setMin()
		self.setMax()

		if self.checkIfTrue():
			result = self.max_price - self.min_price

		# (if not) try removing the current max and recomputing
		self.price_list.remove(self.max_price)
		self.setMax()
		if self.checkIfTrue():
			result = self.max_price - self.min_price

		return result #returns results if self.checkIfTrue(), else just 0 


if __name__ == '__main__':

	cases = [
	[7,1,5,3,6,4],
	[7,6,4,3,1],
	[1],
	[2,4,1],
	]

	for i, case in enumerate(cases):  # step of 2
		s = Solution()
		print(f"___ NO.{i} ___________________________________")
		print(f"n={i} -> {s.maxProfit(case)}\n")

