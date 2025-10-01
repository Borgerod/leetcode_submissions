class Solution:
	def addBinary(self, a: str, b: str) -> str:
		''' the boring answer'''
		return bin(int(a, 2) + int(b, 2))[2:]
		
	def addBinary(self, a: str, b: str) -> str:
		''' the cool answer '''
		a,b = self.bin_to_num(a,b)
		_sum = self.comeGetSum(a,b)
		return self.num_to_bin(_sum)

	def bin_to_num(self, a,b):
		return ((sum(int(bin[i]) * (2 ** (len(bin) - 1 - i)) for i in range(len(bin))))for bin in (a,b))

	def comeGetSum(self, a,b):
		return a+b
	
	def num_to_bin(self, num):
		''' 
			Keep dividing the number by 2 untill its 0, adding all remainders to a list. 
			The binary is the remainders read backwards
		'''
		if not num: return "0"
		int(a, 2)
		r = []
		while N > 0:
			remainder = N % 2
			r.append(str(remainder))
			N = N // 2
		r.reverse()
		return ''.join(r)

if __name__ == '__main__':

	cases=[
		"0",
		"0",
		"10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
		"110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011",
		"11",
		"1",
		"1010",
		"1011",
		"1001",
		"100101",
		"1010010",
		"1111",
		"111011",
		"100",
		"1011011",
		"10111",
		"1000100",
		"1001101",
	]

	for i in range(0, len(cases), 2):  # step of 2
		a, b = cases[i], cases[i+1]
		s = Solution()
		s.addBinary(a,b)
		print(f"n={i} -> {s.addBinary(a,b)}")
		print("\n")
