
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		return str(self.val) + "," + str(self.next)

class Solution:
	def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:	
		short_l, long_l = self.findShortOne(l1, l2)
		l3 = self.addTogether(short_l, long_l)
		return list_to_LL(l3)

	def addTogether(self, short_l, long_l):		
		l3 = []
		reserve = 0
		while long_l:
			if short_l == None:
				x = long_l.val + 0
			else:
				x = long_l.val + short_l.val
			if reserve:
				x += reserve
				reserve = 0
			if x >= 10:
				x = x -10
				reserve += 1
			l3.append(x)
			if short_l == None:
				long_l = long_l.next
			else:
				long_l, short_l = long_l.next, short_l.next
		if reserve:
			l3.append(reserve)	
		return l3

	def findShortOne(self, long_l, short_l):
		len_1, len_2 = self.getLength(long_l), self.getLength(short_l)
		if len_1 -  len_2 != 0:
			if len_1 < len_2:
				short_l, long_l = long_l, short_l
		return short_l, long_l 	

	def getLength(self, lst):
		r = 0
		while lst:
			lst = lst.next
			r += 1
		return r

def list_to_LL(arr):
	if len(arr) < 1:
		return None
	elif len(arr) == 1:
		return ListNode(arr[0])
	return ListNode(arr[0], next=list_to_LL(arr[1:]))





l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# l2 = [9,9,9,9,0,0,0]
l1 = list_to_LL(l1)
l2 = list_to_LL(l2)

s = Solution()
l3 = s.addTwoNumbers(l1,l2)
print(l3)
