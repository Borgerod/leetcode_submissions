class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
	def __repr__(self):
		return str(self.val) + "," + str(self.next)


# class Solution:
# 	def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
# 		length1, length2 = 0, 0 
# 		if list1:
# 			length1 = self.get_length(list1)
# 		if list2:
# 			length2 = self.get_length(list2)
# 		length = self.findGreatestLength(length1, length2)

# 		list3 = self.mergeLists( list1 ,list2, length)
# 		return list_to_LL(list3)


# 	def findGreatestLength(self, length1, length2):
# 		return max(length1, length2)


# 	def mergeLists(self, list1 ,list2, length):
# 		list3 = []		
# 		while list1 or list2:
# 			for i in range(length):
# 				if list3:
# 					if list1.val < list2.val:
# 						print("list1.val < list2.val")
# 						if list1.val > list3[-1]:
# 							list3.append(list1.val)
# 							list3.append(list2.val)
# 						else:
# 							print(False)

# 					elif list1.val > list2.val:
# 						print("list1.val < list2.val")
# 						if list2.val > list3[-1]:
# 							list3.append(list2.val)
# 							list3.append(list1.val)
# 						else:
# 							print(False)
# 					else:
# 						list3.append(list1.val)
# 						list3.append(list2.val)
					
# 				else:
# 					print(False)
# 					if list1:
# 						print('list1 = True')
# 						if list2:
# 							print('list2 = True')
# 							if list1.val < list2.val:
# 								print("list1.val < list2.val")
# 								list3.append(list1.val)
# 								list3.append(list2.val)
# 							elif list1.val > list2.val:
# 								print("list1.val > list2.val")
# 								list3.append(list2.val)
# 								list3.append(list1.val)
# 							else:
# 								list3.append(list1.val)
# 								list3.append(list2.val)
# 						else:
# 							print('only list1 = True')
# 							list3.append(list1.val)
					
# 					elif list2:
# 						print('list2 = True')
# 						if list1:
# 							print('list1 = True')
# 							if list1.val < list2.val:
# 								print("list1.val < list2.val")
# 								list3.append(list1.val)
# 								list3.append(list2.val)
# 							elif list1.val > list2.val:
# 								print("list1.val > list2.val")
# 								list3.append(list2.val)
# 								list3.append(list1.val)
# 							else:
# 								list3.append(list1.val)
# 								list3.append(list2.val)				
# 						else:
# 							print('only list2 = True')
# 							list3.append(list2.val)
				
# 				if list1:
# 					if list1.next != None:
# 						list1 = list1.next
# 				if list2:
# 					if list2.next != None:
# 						list2 = list2.next
			
# 			break
# 		return list3		

# 	def get_length(self, lst):
# 		count = 0
# 		while True:
# 			count += 1
# 			if lst.next != None:
# 				lst = lst.next
# 			else:
# 				return count



class Solution:
	def mergeTwoLists(self, list1: list[ListNode], list2: list[ListNode]) -> list[ListNode]:
		cur = dummy = ListNode()
		while list1 and list2: 
			if list1.val < list2.val:
				cur.next = list1
				list1, cur = list1.next, list1
			else:
				cur.next = list2
				list2, cur = list2.next, list2
		if list1 or list2:
			cur.next = list1 if list1 else list2
		return dummy.next


def list_to_LL(arr):
	if len(arr) < 1:
		return None
	elif len(arr) == 1:
		return ListNode(arr[0])
	return ListNode(arr[0], next=list_to_LL(arr[1:]))



def main():
	list1 = [1,2,4]
	list2 = [1,3,4]
	# list1 = []
	# list2 = []
	# list1 = []
	# list2 = [0]
	# list1 = [1]
	# list2 = []	
	s = Solution()
	result = s.mergeTwoLists(list_to_LL(list1), list_to_LL(list2))
	print(result)


if __name__ == '__main__':
	main()





	# def mergeLists(self, list1 ,list2, length):
	# 	list3 = []
	# 	# while True:
		
	# 	for i in range(length):
	# 		if list3:
	# 			if list1.val < list2.val:
	# 				print("list1.val < list2.val")
	# 				if list1.val > list3[-1]:
	# 					list3.append(list1.val)
	# 					list3.append(list2.val)
	# 				else:
	# 					print(False)

	# 			elif list1.val > list2.val:
	# 				print("list1.val < list2.val")
	# 				if list2.val > list3[-1]:
	# 					list3.append(list2.val)
	# 					list3.append(list1.val)
	# 				else:
	# 					print(False)
	# 			else:
	# 				list3.append(list1.val)
	# 				list3.append(list2.val)
				
	# 		else:
	# 			print(False)
	# 			print(list1.val,list2.val)
	# 			if list1.val < list2.val:
	# 				print("list1.val < list2.val")
	# 				list3.append(list1.val)
	# 				list3.append(list2.val)
	# 			elif list1.val > list2.val:
	# 				print("list1.val > list2.val")
	# 				list3.append(list2.val)
	# 				list3.append(list1.val)
	# 			else:
	# 				list3.append(list1.val)
	# 				list3.append(list2.val)

	# 		if list1.next != None:
	# 			list1 = list1.next
	# 			list2 = list2.next

	# 	print(list3)
	# 	return list3