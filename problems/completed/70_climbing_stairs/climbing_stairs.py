
import math
class Solution:
	''' 
	I saw the numbers was the Fibanocci Sequence, so I used Binet's formula to calculate the answers. 
	Although not dynamic, the runtime was O(1)
	'''
	
	@property
	def phi(self):
		return (1+math.sqrt(5))/2

	def climbStairs(self, n: int) -> int:
		''' '''
		return int(((self.phi ** (n+1)) - ((1 - self.phi) ** (n+1))) / math.sqrt(5))



if __name__ == '__main__':

	cases=[
		45,
		33,
		2,
		3,
		4,
		5,
		6,
		7,
		8,
		9,
	]

	for n in cases:
		
		s = Solution()
		print(f"n={n} -> {s.climbStairs(n)}")
		