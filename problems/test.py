class solution:
	def __init__(self) -> None:
		self.price_list = [900,510,174,329,873,382,279,855,396,810,322,192,442,775,445,861,303,975,478,543,87]
		self.backup = self.price_list
		self.max_price = 0
		self.min_price = 0
		self.result = 0

	def setMin(self, ):
		self.min_price = min(self.price_list, default=0)

	def setMax(self, ):
		self.max_price = max(self.price_list, default=0)
		
		print(self.price_list)

	def maxProfit(self, ):
		print(self.max_price)
		print(self.min_price)
		print(self.price_list)
		if self.checkIfTrue():
			print(f"{self.price_list.index(self.max_price)} > {self.price_list.index(self.min_price)}")
			self.result = self.max_price-self.min_price
		else:
			self.backup = self.price_list 
			self.price_list.remove(self.max_price)
			self.setMax()


	def maxProfit(self, ):
		print(self.max_price)
		print(self.min_price)
		print(self.price_list)
		if self.checkIfTrue():
			print(f"{self.price_list.index(self.max_price)} > {self.price_list.index(self.min_price)}")
			self.result = self.max_price-self.min_price
		else:
			self.backup = self.price_list 
			self.price_list.remove(self.max_price)
			if self.checkIfTrue():
				self.result = self.max_price-self.min_price	
						
			self.setMax()
	

			self.maxProfit()

	def checkIfTrue(self, ):
		return self.price_list.index(self.max_price) > self.price_list.index(self.min_price)

s = solution()
s.setMin()
s.setMax()
s.maxProfit()
print(f" ==> {s.result}")
