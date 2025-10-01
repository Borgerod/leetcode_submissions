class Solution:
	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		'''
		time_complexity : O(log(m+n))
		Median: The middle number;
		'''
		median_point = (len(nums1) + len(nums2)) / 2  # integer division for index
		# Merge two sorted lists
		merged = []
		i = j = 0
		is_odd=True
		print(median_point)
		if median_point.is_integer():
			is_odd=False
		print("nums1+nums2: ", nums1+nums2)
		if nums1 and nums2:
			while i < len(nums1) and j < len(nums2):
				if i >= len(nums1) or j >= len(nums2):
					break

				if len(merged)>=median_point:
					print("point is reached")
					merged.append(nums2[j])
					print(merged)
					if is_odd:
						print("is_odd")
						return merged[-1]
					else:
						print("is_not_odd")
						print(f"({merged[-1]}+{merged[-2]}/2) = {(merged[-1]+merged[-2])/2}")
						return (merged[-1]+merged[-2])/2
				
				if nums1[i] < nums2[j]:
					merged.append(nums1[i])
					i += 1
				else:
					merged.append(nums2[j])
					j += 1

		merged.extend(nums1[i:])
		merged.extend(nums2[j:])

		if is_odd:
			print("is_odd 2")
			return merged[-2]
		else:
			print("is_not_odd 2")
			print(f"({merged[-2]}+{merged[-3]}/2) = {(merged[-2]+merged[-3])/2}")
			return (merged[-2]+merged[-3])/2

		# Append any remaining elements
		# print(merged)


		# m = len(nums1)
		# n = len(nums2)
		# nm = len(nums2 + nums1)
		# print(nm)
		# i = 0
		# # nums3 = []
		# # print("nums1+nums2: ", nums1+nums2)
		# # while i < nm:
		# # 	print(i)




		# # 	if i >= n:
		# # 		nums3.extend(nums1[i:])
		# # 		break

		# # 	elif i >= m:
		# # 		nums3.extend(nums2[i:])
		# # 		break
			
		# # 	if nums1[i] <= nums2[i]:
		# # 		if nums1[i] > nums3[-1]:
		# # 			nums3.extend([nums1[i], nums2[i]])
		# # 		else:


		# # 	else: 
		# # 		nums3.extend([nums2[i], nums1[i]])


		# # 	i += 1

		# median_point = nm/2
		# y=0
		# i=0
		# print(f"median_point: {median_point}")
		# print("nums1+nums2: ", nums1, nums2)
		# # print("nums1+nums2: ", nums1+ nums2)
		# # while i < nm:
		# # 	print(f"i: {i}")
		# # 	if i >= (median_point):
		# # 		print("median reached")
		# # 		if median_point.is_integer():
		# # 			print(f"	nums1: {nums1}")
		# # 			print("	nums1[0]: ", nums1[0])
		# # 			print("	nums1[-1]: ", nums1[-1])
		# # 			print("	(nums1[-1]+nums1[-2])/2: ", ((nums1[-1]+nums1[-2])/2))
		# # 			return (nums1[-1]+nums1[-2])/2
		# # 		else:
		# # 			print("	nums1[-2]: ", nums1[-2])
		# # 			return nums1[-2]
		# # 			# (nums1[-1]+nums1[-2])/2

		# # 	# while nums2[y] < nums1[i]:
		# # 	# 	i+=1
		# # 	# 	if i+1>=m:
		# # 	# 		nums1+nums2[y:]
		# # 	# 	if nums2>=nums1[i]:
		# # 	# 		nums1.insert(i + 1, nums2[y])
			
		# # 	if nums1[i] <= nums2[y]:
		# # 		print(f"	nums1[i] <= nums2[y]: {nums1[i]} <= {nums2[y]}")
		# # 		print("	(i+1): ",(i+1))

		# # 		if y >= n:
		# # 			print( f"	error: y+1>=n {y+1} >= {n}")
		# # 			break

		# # 		if (i+1) >= m:
		# # 			print(f"	(i+1) >= m: {(i+1)} >= {m}")
		# # 			nums1.append(nums2[y])
		# # 		else:
		# # 			print(f"	(i+1) < m: {(i+1)} < {m}")
		# # 			if nums1[i+1] > nums2[y]:
		# # 				nums1.insert(i + 1, nums2[y])
		# # 			else:
		# # 				print("i+1 is smaller than y, jump ahead")
		# # 				i+=1
		# # 				nums1.insert(i + 1, nums2[y])

		# # 			# nums1[i+1] = nums2[y]
		# # 			# nums1.insert(nums2[y], i)
		# # 		print(nums1, "\n")
		# # 		y += 1
		# # 		i += 1
		# # 	else:

		# # 		i += 1
		# # 		# y += 1



		# 	# if i >= n:
		# 	# 	nums3.extend(nums1[i:])
		# 	# 	break

			
		# median_point = nm/2
		# is_odd = True
		# if median_point.is_integer():
		# 	is_odd = False
		# y=0
		# i=0
		# print(f"median_point: {median_point}")
		# print("nums1+nums2: ", nums1, nums2)
		# print("nums1+nums2: ", nums1+ nums2)

		# # for i in range(0,int(median_point)):
		# while i < int(median_point):
		# 	print(f"i:{i}, y:{y}")
		# 	if i >= m:
		# 		nums1.extend([nums2[y]])
		# 		y+=1
		# 		i+=1
		# 	if nums1[i]<nums2[y]:
		# 		y+=1
		# 		i+=1
		# 	else: y+=1
			
		# 	if i >= (median_point):
		# 		print("median reached")
		# 		if median_point.is_integer():
		# 			# print(f"	nums1: {nums1}")
		# 			# print("	nums1[0]: ", nums1[0])
		# 			# print("	nums1[-1]: ", nums1[-1])
		# 			# print("	(nums1[-1]+nums1[-2])/2: ", ((nums1[-1]+nums1[-2])/2))
		# 			return (nums1[-1]+nums1[-2])/2
		# 		else:
		# 			# print("	nums1[-2]: ", nums1[-2])
		# 			return nums1[-2]
		# 			# (nums1[-1]+nums1[-2])/2

			
		# print("nums1: ",nums1)



if __name__ == '__main__':

	cases = [
		[1,6],
		[2,4,5,5],
		[1,3],
		[2],
		[1,2],
		[3,4],
		[1,3],
		[1],
		[],
	]

	for i in range(0, len(cases), 2):  # step of 2
		nums1, nums2 = cases[i], cases[i+1]
		s = Solution()
		print(f"___ NO.{i} ___________________________________")
		
		print(f"n={i} -> {s.findMedianSortedArrays(nums1, nums2)}")
		print("\n")

