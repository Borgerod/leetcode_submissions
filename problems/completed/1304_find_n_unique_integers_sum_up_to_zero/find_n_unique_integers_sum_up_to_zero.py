class Solution:

	def sumZero(self, n: int) -> list[int]:
		''' 
			n : amount if unique ints
			_n: half of n -> half negative half positive. if float == odd == apppend a final 0
			is_odd: check if odd. if float == odd == apppend a final 0
			sum_zero: list of unique ints, where sum == 0
		'''
		_n = n/2
		is_odd = True
		if _n.is_integer():
			# is int / even number
			is_odd = False
		# else: is float / odd number
	
		sum_zero = [i for i in range(1,int(_n)+1)] + [-i for i in range(1,int(_n)+1)]
		if is_odd:
			sum_zero.append(0)

		if sum(sum_zero)==0 and len(set(sum_zero))==len(sum_zero)==n:
			return sum_zero
		else:
			print("ERROR")


	def sumZero(self, n: int) -> list[int]:
		#* CLEANER VERSION
		''' 
			n : amount if unique ints
			_n: half of n -> half negative half positive. if float == odd == apppend a final 0
			is_odd: check if odd. if float == odd == apppend a final 0
			sum_zero: list of unique ints, where sum == 0
		'''
		limit = int(n / 2) + 1
		sum_zero = [0] * (2 * (limit - 1))  # pre-allocate exact size
		for i in range(1, limit):
			sum_zero[2*(i-1)] = i
			sum_zero[2*(i-1) + 1] = -i
		
		if (n/2).is_integer():
			return sum_zero
		sum_zero.append(0)
		return sum_zero
		
			



		
	




if __name__ == '__main__':

	cases = [
		5,
		3,
		1,
		# 999,
		# 800,
		# 487,
		# 23,
		# 912,
	]

	for i, n in enumerate(cases):  # step of 2
		
		s = Solution()
		print(f"___ NO.{i} ___________________________________")
		# s.sumZero(n)
		# print(f"n={i} -> {s.sumZero(n)}")
		sum_zero = s.sumZero(n)
		print("res:", sum_zero)
		print("n: ",n, n==len(sum_zero))
		# print("len(): ", len(sum_zero), len(sum_zero)==len(set(sum_zero)))
		# print("len(set()): ", len(set(sum_zero)))
		# print("sum(): ", sum(sum_zero), sum(sum_zero)==0)
		# if sum(sum_zero)==0 and len(set(sum_zero))==len(sum_zero) and len(sum_zero)==n:
		# 	print("\n	==> Success")
		# else:
		# 	print("\n	==> ERROR")
		print("\n")
