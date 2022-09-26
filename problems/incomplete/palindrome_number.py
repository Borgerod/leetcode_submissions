'''
	what is palindrome?
	a phrase that can be read both ways: 
	otto
	poop
	1881
	666 

	NOTE:
		odd numbers like, 121 counts.
'''
class Solution:
	def isPalindrome(self, x: int) -> bool:
		checklist = [True for index, i in enumerate(str(x)) if i in str(x)[-index-1]]
		return len(checklist) == len(str(x))

def main():
	inputs = [-121, 121, 10 , 1881]
	'''
		fasit: [True, False, False, True]
	'''
	s = Solution()
	for x in inputs:
		result = s.isPalindrome(x)
		print(result)

if __name__ == '__main__':
	main()