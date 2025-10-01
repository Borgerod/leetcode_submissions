# > WORKSHOP VERSION
class Solution:
	'''
	#* Rule: everything except leetcoded submissions are allowed and ai using leetcode submissions.
	#* Rule: I will try and solve this as fast as possible. No optimisation
	#* Note: Time includes; ['reading task', 'panick', 'building', 'pushing', 'testing', 'research', 'breaks', ] | Time excludes; ['prepping files', 'writing description', '', '', '', ]
	
	no-zero-int = int that is; positive, do not contain any "0", i.e.:
	#!      100: X
	#!      -99: X
	#!        0: X
	#*       99: v

	input:  n (2 <= n => 10000)
	output: [a, b] -> a + b = n
	NOTE: A case CAN have multiple correct solutions, you only need to return ONE of them. 
	'''
	def isNonZero(self, num:int) -> bool:
		return "0" not in str(num)

	def isPositive(self, num:int) -> bool:
		return num > 0
	
	def getNoZeroIntegers(self, n: int) -> list[int]:
		n = n #temp (the answer)
		a = 1 #solution 1
		b = 1 #solution 2
		# NOTE: a sn b do not have to be unique, so i should check if n/2 is possible first. 
		if (n/2).is_integer():
			if self.isNonZero((n/2)):
				print(f"Valid, n/2 ({n}/2={n/2}) has NO 0 ")
				return [n/2, n/2]  #given n is also a non-zero
			else:
				print("Invalid, n/2 contains 0 ")

		while a < n:
			print(f"	a:{a}")
			# if self.isNonZero(a) and self.isPositive(b):
			if self.isNonZero(a):
				print("			valid, a NOT contain 0")
				if self.isPositive(a):
					print("			valid, a>0 ")

					b = n-a
					print(f"	b: {b}")
					if self.isNonZero(b) and self.isPositive(b):
						print("			valid, b NOT contain 0 AND b>0 ")
						return [a,b]
					else:
						print("			invalid, b contain 0 OR b<0 --> a+=1")
						a+=1	
			else:
				print("		invalid, a contain 0 OR a<0	--> a+=1")
				a+=1
		
		print(f"ERROR: \n a == n [{a} == {n}] without finding a valid answer")
			  

		return [a,b] 
		
	
# * CLEAN VERSION
class Solution:
	def isNonZero(self, num:int) -> bool:
		return "0" not in str(num)

	def isPositive(self, num:int) -> bool:
		return num > 0
	
	def getNoZeroIntegers(self, n: int) -> list[int]:
		a = 1 #solution 1
		b = 1 #solution 2
		if (n/2).is_integer() and self.isNonZero((n/2)):
				return [n/2, n/2]  #given n is also a non-zero

		while a < n:
			if self.isNonZero(a) and self.isPositive(a) and self.isNonZero((n-a)) and self.isPositive((n-a)):
				return [a,n-a]
			else:
				a+=1	
		return [a,b] 
		
	




if __name__ == '__main__':

	cases = [

			
			2,
			11,

			9,
			23,
			123,
			567,
			5678,
			1234,
			2349,
			9999,
	]
	#> OPTION 1 (for single inputs)
	s = Solution()
	for i, n in enumerate(cases):
		print(f"___ NO.{i} ___________________________________")
		print(f"n={i} -> {s.getNoZeroIntegers(n)}\n")

