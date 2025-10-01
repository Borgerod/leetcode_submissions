def limited_print(lst, limit=6):
	if len(lst) <= 2 * limit:
		return lst
	else:
		return f"{lst[:limit]} ... {lst[-limit:]} (total {len(lst)})"
class Solution:

	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		a=nums1
		b=nums2
		print(f"a: {a}, b: {b}")
		n=len(a)
		m=len(b)
		median_point = (len(a) + len(b)) / 2
		# is_odd = True if median_point.is_integer() else False
		is_odd = True
		print(f"*** median_point {median_point}")
		mp = median_point
		if median_point.is_integer() and median_point!=0:
			is_odd = False
			median_point+=1
		# 	mp+=1
		# else:
		mp+=1	

		i,j = 0,0
		nums = []
		print(f"is_odd: {is_odd}")
		# while mp>=1:
		# 	print(f"mp:{mp} i:{i}")
		# 	if i==n or j==m:
		# 		print("error i==n or j==m")
		# 		print(nums)
		# 		break
		
		# 	if (i+1) >= n:
		# 		print("error i>=(n-1)")
		# 		print(nums)

		# 		break
		
		# 	if (i+1)<n:
		# 		if a[i]<b[j]<a[i+1]:
		# 			nums += [a[i], b[j]]
		# 			i+=1 
		# 			j+=1
		# 			mp-=2
				
		# 		elif a[i]>b[j]<a[i+1]:
		# 			nums.append(b[j])
		# 			j+=1
		# 			mp-=1
				
		# 		elif a[i]<b[j]>a[i+1]:
		# 			nums.append(a[i])
		# 			i+=1
		# 			mp-=1
		# 		else:
		# 			print(f"{a[i]} {b[j]} {a[i+1]}")
		# 			print("ERROR")
		# 			break
		# 	# else:
		# 	# 	print(f"merged: {nums}")
		# 	# 	print(f"median point: {median_point}")
		# 	# 	break
		# # ...existing code...
					
		# while mp >= 1:

		while mp > 0.5:
			print(f"mp:{mp} i:{i} j:{j}")
			# If both arrays have elements left
			if i < n and j < m:
				if a[i] <= b[j]:
					nums.append(a[i])
					i += 1
				else:
					nums.append(b[j])
					j += 1
				mp -= 1
			# If a is exhausted, take from b
			elif i == n and j < m:
				nums.append(b[j])
				j += 1
				mp -= 1
			# If b is exhausted, take from a
			elif j == m and i < n:
				nums.append(a[i])
				i += 1
				mp -= 1
			# else:
			# 	break
			print(f"merged: {nums}")
			print(f"median point: {median_point}")
		print(nums)
		if nums:
			if is_odd:
				return nums[-1]
			else:
				return (nums[-1]+nums[-2])/2 if len(nums)>=2 else nums[0]
		else:	
			if a:
				return a[0]
			else:
				return b[0]
		# while mp >1:
		# 	print(f"mp:{mp} i:{i}")
		# 	if i == n or j == m:
		# 		print("error i==n or j==m")
		# 		print(nums)
		# 		break
		
		# 	if i > n:
		# 		print("error i>=(n-1)")
		# 		print(nums)
		# 		break
		
		# 	if i < n:
		# 		# Check if i+1 is within bounds before accessing a[i+1]
		# 		if (i + 1 < n) and a[i] < b[j] < a[i + 1]:
		# 			nums += [a[i], b[j]]
		# 			i += 1
		# 			j += 1
		# 			mp -= 2
		
		# 		elif (i + 1 < n) and a[i] > b[j] < a[i + 1]:
		# 			nums.append(b[j])
		# 			j += 1
		# 			mp -= 1
		
		# 		elif (i + 1 < n) and a[i] < b[j] > a[i + 1]:
		# 			nums.append(a[i])
		# 			i += 1
		# 			mp -= 1
		# 		# else:
		# 		# 	print(f"No condition matched for a[i]={a[i]}, b[j]={b[j]}, i={i}, j={j}")
		# 		# 	print("Breaking to avoid infinite loop.")
		# 		# 	print(f"merged: {nums}, {a}, {b}")
		# 		# 	print(f"median point: {median_point}")
		# 		# 	break
		
		# 	elif i==n:
		# 		nums.append(a[i])
		# 		i += 1
		# 		mp -= 1
		# 		print(f"No condition matched for a[i]={a[i]}, b[j]={b[j]}, i={i}, j={j}")
		# 		print("Breaking to avoid infinite loop.")
		# 		print(f"merged: {nums}, {a}, {b}")
		# 		print(f"median point: {median_point}")
		# 		break
		
		# 	else:
		# 		#i is empty
		# 		nums.append(b[j])
		# 		j += 1
		# 		mp -= 1
		# 	print(f"merged: {nums}")
		# 	print(f"median point: {median_point}")

	# def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
	# 	'''
	# 	time_complexity : O(log(m+n))
	# 	Median: The middle number;
	# 	'''
	# 	median_point = (len(nums1) + len(nums2)) / 2  # integer division for index
	# 	# Merge two sorted lists
	# 	merged = []
	# 	i = j = 0
	# 	is_odd = True
	# 	print(f"median_point after: {median_point}")
	# 	if median_point.is_integer():
	# 		# print(f"TRUE {median_point} is an INTEGER, making len(list) an EVEN number")
	# 		is_odd = False
	# 	# else:
	# 	# 	print(f"FALSE {median_point} is NOT an INTEGER, making len(list) an ODD number")
	# 		# median_point = int(median_point)+1
	# 	print(f"median_point after: {median_point}")
	# 	print(f"is_odd={is_odd}")
	# 	print(f"nums1, nums2: {limited_print(nums1), limited_print(nums2)}")
	# 	print(f"nums1+nums2: {limited_print(nums1+nums2)}")
		
	# 	# if len(nums1+nums2)>=2:
	# 	# 	print("YEHAW")
	# 	# else:
	# 	# 	print("NEYHAW")
			
	# 	if nums1 and nums2 and len(nums1+nums2)>=2:
	# 		while i < len(nums1) and j < len(nums2):
	# 			# print(f"i:{i}")
	# 			# if i >= len(nums1) or j >= len(nums2):
	# 			# 	print("median_point was NOT reached")
	# 			# 	print(f"merked before breaking loop: {limited_print(merged)}")
	# 			# 	break
				

	# 			if len(merged) >= median_point:
	# 				print("median_point is reached")
	# 				merged.append(nums2[j] if nums2[j]<nums1[i] else nums1[i])
	# 				if is_odd:
	# 					print("is_odd")
	# 					print(f"merged: {limited_print(merged)}")
	# 					print("** RETURNED @46")
	# 					return merged[-1] #last item in list
					
	# 				elif not is_odd and len(merged) >= 2:
	# 					print("is_not_odd")
	# 					print(f"({merged[-1]}+{merged[-2]}/2) = {(merged[-1]+merged[-2])/2}")
	# 					print(f"merged: {limited_print(merged)}")
	# 					print("** RETURNED @53")
	# 					return (merged[-1]+merged[-2])/2

				

	# 			if nums1[i] < nums2[j]:
	# 				# print("median_point was NOT reached -> nums1[i] < nums2[j]")
	# 				merged.append(nums1[i])
	# 				# print(f"merged: {limited_print(merged)}")
	# 				i += 1

	# 			else:
	# 				# print("median_point was NOT reached -> nums1[i] > nums2[j]")
	# 				merged.append(nums2[j])
	# 				j += 1
	# 		if not is_odd: #is even
	# 			#find which one exeeded
	# 			if i==len(nums1):
	# 				# print("*it was i")
	# 				# z = int(median_point)-len(merged)
	# 				# print(len(nums2))
	# 				# print(len(nums2[j:]))
	# 				# return (nums2[j:][z] + nums2[j:][z-1])/2 
	# 				if nums2[j] >= nums1[-1]:
	# 					print("	nums2[j]>=nums1[-1]")
	# 					merged.append(nums2[j])
	# 				else:
	# 					print("	nums2[j]<nums1[-1]")
	# 					merged[i-1] = nums2[j]
					
	# 			elif j == len(nums2):
	# 				print("*it was j")
	# 				if nums1[i] >= nums2[-1]:
	# 					print("	nums1[i]>=nums2[-1]")
	# 					merged.append(nums1[i])
	# 				else:
	# 					print("	nums1[i]<nums2[-1]")
	# 					merged[j-1] = nums1[i]
	# 			print(f"	final merged (EVEN): {limited_print(merged)}")
	# 			print("** RETURNED @88")
	# 			return (merged[-1] + merged[-2])/2
			
	# 		else:
	# 			print(f"	final merged (ODD): {limited_print(merged)}")
	# 			print("** RETURNED @92")
	# 			return merged[int(median_point)] if merged else 0

				

							
	# 	else:
	# 		print(f"list < 2 or is lacking: {limited_print(merged)}")
	# 		merged.extend(nums1[i:])
	# 		merged.extend(nums2[j:])
	# 	return merged[int(median_point)] if merged else 0
	# 	# merged.extend(nums1[i:])
	# 	# merged.extend(nums2[j:])

	# 	# if is_odd:
	# 	# 	print("is_odd 2")
	# 	# 	return merged[-2]
	# 	# else:
	# 	# 	print("is_not_odd 2")
	# 	# 	print(f"({merged[-2]}+{merged[-3]}/2) = {(merged[-2]+merged[-3])/2}")
	# 	# 	return (merged[-2]+merged[-3])/2
	# 	# print(f"merged: {limited_print(merged)}")
	# 	# if len(merged) >= 2:
	# 	# if not is_odd and len(merged) >= 2:
	# 	# 	print("** RETURNED @113")
	# 	# 	return (merged[-1] + merged[-2])/2
	# 	# else:
	# 	# 	# Handle edge case: not enough elements
	# 	# 	print("** RETURNED @117")
	# 	# 	return merged[int(median_point)] if merged else 0


if __name__ == '__main__':

	cases = [
[0,0,0,0,0],
[-1,0,0,0,0,0,1],				
[1000000],
[-1000000],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
[1, 3, 5, 7, 9],
[2, 4, 6, 8, 10, 12],
[1],
[2, 3, 4, 5, 6, 7, 8, 9, 10],
[5, 5, 5, 5, 5],
[5, 5, 5, 5, 5],
	]
	solutions = [
		0.0,        # [0,0,0,0,0], [-1,0,0,0,0,0,1]
		0.0,        # [1000000], [-1000000]
		10.5,       # [1,2,3,4,5,6,7,8,9,10], [11,12,13,14,15,16,17,18,19,20]
		6.0,        # [1,3,5,7,9], [2,4,6,8,10,12]
		5.5,        # [1], [2,3,4,5,6,7,8,9,10]
		5.0,        # [5,5,5,5,5], [5,5,5,5,5]
	]

	s = Solution()
	for i in range(0, len(cases), 2):
		print(f"___ NO.{i} ___________________________________")
		nums1, nums2 = cases[i], cases[i+1]
		output = s.findMedianSortedArrays(nums1, nums2)
		solution = solutions[i // 2]  # Use integer division to get the correct solution index
		print(f"n={i} -> {output}")
		print(f"solution: {solution}")
		if solution == output:
			print("	ACCEPTED")
		else:
			print("	NOT ACCEPTED")
		print("\n")	

