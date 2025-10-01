#* ACCEPTED; CLEAN VERSION
class Solution:
	def findContentChildren(self, g: list[int], s: list[int]) -> int:
		s.sort(), g.sort()
		content_counter,i,y = 0,0,0
		while i < len(s):
			if y == len(g): break
			if s[i] >= g[y]:
				y+=1; content_counter+=1
			i+=1
		return content_counter


class Solution:
	
	# def findContentChildren(self, g: list[int], s: list[int]) -> int:
	# 	# todo make pointers
	# 	# todo parse lists

		
	# 	print("SORTING:")
	# 	g = self.sortList(g)
	# 	s = self.sortList(s)

	# 	print(f"Start: cookies: {s}")
	# 	print(f"Start: children: {g}")
	# 	if len(s)==0 or len(g)==0:
	# 		return 0 
	# 	print(s[0])
	# 	print(g[0])
	# 	if len(s) < len(g):
	# 		# imin = big.index(small[0])
	# 		if g.index(s[0]):
	# 			g = g[g.index(s[0]):]
	# 	else:
	# 		if s.index(g[0]):
	# 			s = s[s.index(g[0]):]
			
	# 	# 	s = s 
	# 	# 	g = g
	# 	# else:
	# 	# 	s = g
	# 	# 	g = s

	# 	# s[0]
	# 	# imin = g.index(s[0])
	# 	# g = g[imin:]
	# 	# imax = g.index(s[-1])
	# 	self.content_counter = 0 
	# 	y = 0
	# 	i = 0
	# 	# print(g)
	# 	# print(s)

	# 	while i < len(s):
	# 		if y == len(g) or i == len(s):
	# 			break
	# 			# y == 0
	# 		if s[i] >= g[y]:
	# 			# print(s[i])
	# 			# print(g[i])
	# 			print(f"s({s[i]}) >= g({g[y]})")
	# 			self.content_counter += 1
	# 			i += 1
	# 			y += 1

				
	# 		else:
	# 			print("else")
	# 			y += 1
			

	# 	return self.content_counter

	# 	# gl, gr = 0 , len(g) - 1 #pointers for g 
	# 	# sl, sr = 0 , len(s) - 1 #pointers for s
	# 	# content_child = 0 #counter
	# 	# i = 0
	# 	# while sl <= sr: #iterate cookies first
	# 	# 	print(f"i: {i}")
	# 	# 	i_i = 0
	# 	# 	# while gl <= gr:
			
	# 	# 	for i_i, gl in enumerate(g):
	# 	# 		print(f"	i_i: {i_i}")
	# 	# 		if isinstance(s[sl], int) and isinstance(gl, int) and self.isContent(size = s[sl], greed = gl):
	# 	# 			content_child += 1
	# 	# 			# s.pop(sl)
	# 	# 			# g.pop(gl)
	# 	# 			s[sl]=""
	# 	# 			g[i_i]="" 
	# 	# 			# g{i_i}
	# 	# 			print(f"	found match on: {i}({i_i}) for s[sl] = g -> {s[sl]} = {gl} assigning child 1 cookie")
					
	# 	# 		else:
	# 	# 			print(f"	no match -> check next")
	# 	# 		# gl += 1 

	# 	# 		# print("	gl < gr? ", gl<gr)
	# 	# 		print("\n")

	# 	# 	i += 1
	# 	# 	sl += 1 

	# 	# 	print("sl < sr? ", sl<sr)
			
		
	# 	# print(f"content_child: {content_child}")
	# 	# print(f"rest of children: {g}, rest of cookies: {s}")


	# 	# return content_child


	# # def sortList(self, li:list[int]) -> list:
	# # 	left, right = 0 , len(li) - 1

	# # 	while left < right and len(li)>1:
	# # 		print(f"	left, right: {left, right}")
	# # 		if li[left] >= li[right]:
	# # 			print(f"		left({li[left]}) >= right({li[right]})")
	# # 			if li[left] > li[left+1]:
	# # 				print(f"			left({li[left]}) > left+1({li[left+1]})")
	# # 				#too g to be left
	# # 				li.append(li[left])
	# # 				li.pop(left)

	# # 			elif li[right] < li[right-1]:
	# # 				print(f"			left({li[right]}) < left+1({li[right-1]})")
	# # 				li.insert(0, li[right])
	# # 				li.pop(right)
	# # 			print(li)
	# # 			left, right = 0 , len(li) - 1
	# # 		# elif li[left] == li[right]:   #[ 10,2,3,4,10 ] [ 1,20,30,40,1 ]
	# # 		# 	if li[left-1] and li[left] < li[left-1]:
	# # 				# if li[right+1] and li[right] > li[right+1]:
	# # 		# left, right = 0 , len(li) - 1
	# # 		left += 1 
	# # 		right -= 1
	# # 	return li
	

	# # !ORIGINAL
	# def sortList(self, li:list[int], g) -> list:
	# 	for i in range(len(li)):
	# 		for j in range(len(li) - i - 1):
	# 			if li[j] > li[j + 1]:
	# 				# swap like using pointers
	# 				li[j], li[j + 1] = li[j + 1], li[j]

	# 				#then check if its bigger than the
	# 				#> sudo: if li == "s" (if they are the  s list and not g list)
	# 				li[j+1] #the bigger number
	# 				#? if li == g scenario
	# 				for _g in g:
	# 					if li[j+1]<_g:
	# 						self.content_counter += 1
							
						
	# 				#? if li == g scenario
	# 				for _s in s:
	# 					if li[j+1]>_s:
	# 						self.content_counter += 1
	# 	return li
	


	def findContentChildren(self, g: list[int], s: list[int]) -> int:
		# todo make pointers
		# todo parse lists
		print("	dataset, start:")
		print(f"	Children:{g}")
		print(f"	Cookies:{s}")
		print("	--------------------------------------")
		
		
		print("	Sorted:")
		self.content_counter = 0
		# g = self.sortList(li=g)
		# temp
		# g = [1, 2, 4, 10, 10, 222]
		# print(g)
		s = self.sortList(s)
		for i in s:
			if i >= min(g):
				self.content_counter+=1
				g.remove(min(g))
		print(self.content_counter)

	def findContentChildren(self, g: list[int], s: list[int]) -> int:
		# todo make pointers
		# todo parse lists
		print("	dataset, start:")
		print(f"	Children:{g}")
		print(f"	Cookies:{s}")
		print("	--------------------------------------")
		
		
		print("	Sorted:")
		# g = self.sortList(li=g)
		# temp
		# g = [1, 2, 4, 10, 10, 222]
		# print(g)
		content_counter = 0
		s.sort(), g.sort()
		print(f"	Children:{g}")
		print(f"	Cookies:{s}")
		i=0
		y=0
		while i < len(s) and y < len(g):
			if s[i]>=g[y]:
				print(f"{s[i]}>={g[y]}")
				i+=1
				y+=1
				content_counter+=1
			else:
				print(f"{s[i]}<{g[y]}")
				i+=1
		return content_counter
	
		# g.remove(min(g))
		# g=g[s.index(min(s)):s.index(max(s))]
		# print(g[0:])
		# print(s.index(min(s)))
		# print(g)

		# # * OPTION 1
		# self.content_counter = 0
		# s = self.sortList(s)
		# for i in s:
		# 	if i >= min(g):
		# 		self.content_counter+=1
		# 		g.remove(min(g))
		# print(f"Option 1: {self.content_counter}")

		# # * OPTION 2
		# self.content_counter = 0
		# lenS=len(s)
		# i=0
		# while i<lenS:
		# 	if s[i] > min(g):
		# 		self.content_counter+=1
		# 		g.remove(min(g))
		# 	i+=1
		# print(f"Option 2: {self.content_counter}")
			
		# # * OPTION 3
		# self.content_counter = 0
		# lenS=len(s)
		# i = 0
		# while i < lenS:
		# 	if not s:
		# 		break
		# 	print("x", min(s))
		# 	print(f"cookie_size:{min(s)} >= kid_greed:{min(g)} : {min(s) >= min(g)}")
		# 	print(f"	cookie_size: {s} , kid_greed: {g}")
		# 	print("\n")
		# 	if min(s) >= min(g):
		# 		self.content_counter+=1
		# 		g.remove(min(g))
		# 		s.remove(min(s))
		# 		continue
		# 	s.remove(min(s))
		# print(f"Option 3: {self.content_counter}")

		# # * OPTION 4
		# self.content_counter = 0
		# lenG=len(g)
		# i = 0
		# while i < lenG:
		# 	if not g:
		# 		break
		# 	print("x", max(g))
		# 	print(f"kidgreed:{max(g)} <= cookiegize:{max(s)} : {max(g) <= max(s)}")
		# 	print("\n")
		# 	# if max(s) <= max(g):
		# 	if max(g) <= max(s):
		# 		self.content_counter+=1
		# 		s.remove(max(s))
		# 		g.remove(max(g))
		# 		continue
		# 	g.remove(max(g))
		# 	print(f"	kidgreed: {g} , cookiegize: {s}")
		# print(f"Option 3: {self.content_counter}")



	# def sortList(self, li:list[int], g = None ) -> list:
	# 	print(g)
	# 	if g:
	# 		print("\nsorting++ cookies:")
	# 		_g = list(reversed(g))
	# 	for i in range(len(li)):
	# 		for j in range(len(li) - i - 1):
	# 			print(f"	c:{j}")
	# 			if li[j] > li[j + 1]:
	# 				print(f"	if li[{li[j]}] > li[{li[j + 1]}]: True")
	# 				# swap like using pointers
	# 				li[j], li[j + 1] = li[j + 1], li[j]
					
	# 				if g: #if li: s-list and g-list is the sublist
	# 					# print("		if g: True")
	# 					#sort + find biggest match	
	# 					#? if li == g scenario
	# 					biggest_g = 0
	# 					for i in range(len(_g)):
	# 						# if li[j+1]<_g:
	# 						if li[j] >= _g[i]:
	# 							print(f"		if li[{li[j]}]  >=  _g[{_g[i]}]: True")
	# 							biggest_g = _g[i]
								
	# 					if biggest_g>0:
	# 						_g[i] = 30001
	# 						# _g[i].pop()
	# 						# _g.pop(i)
	# 						self.content_counter += 1
	# 						print(f"				counter += 1 --> {self.content_counter}")
	# 						print(f"				_g updated: {_g}")
	# 						print(f"				li updated: {li}")
	# 				else:
	# 					print("		if g: False")	
	# 				#else: first one, sort it normally
	# 			if g:
	# 				print("		if g: True")
	# 				#sort + find biggest match	
	# 				#? if li == g scenario
					
					
	# 				# print("			ZZZZ", _g)
	# 				for i in range(len(_g)):
	# 				# for i in range(len(g) - 1, -1, -1):
	# 					# if li[j+1]<_g:
	# 					# print(f"			ZZZZ len(g): {len(_g)}")
	# 					# print(f"			ZZZZ g[0]: {_g[0]}")
	# 					# print(f"			ZZZZ g[-1]: {_g[-1]}")
	# 					# print(f"			ZZZZ i: {i}")
	# 					# print("		_________________________")
	# 					if li[j] >= _g[i]:
	# 						print(f"		if li[{li[j]}]  >=  g[{_g[i]}]: True")
	# 						_g[i] = 30001 #highest possible number
	# 						li[j] = 0 
	# 						# _g.pop(i)
	# 						# li.pop(j)
	# 						self.content_counter += 1
	# 						print(f"				counter += 1 --> {self.content_counter}")
	# 						print(f"				_g updated: {_g}")
	# 						print(f"				li updated: {li}")
							
	# 						break
	# 				else:
	# 					print("			if g: False")	
	# 	print("\n")
	# 	if g:
	# 		print(f"	kid_greed:{g}")
	# 		print(f"	kid_greed:{_g}")
	# 		print(f"	Cookie_size:{li}")
	# 	else:
	# 		print(f"	kid_greed:{li}")
	# 	return li
	'''
	kid_greed:		[1, 2, 4, 10, 10, 222]
	Cookie_size:	[1, 2, 3, 6, 6, 100]

	kid_greed:		[222, 10, 10, 30001, 30001, 30001]
	Cookie_size:	[0, 0, 1, 3, 6, 100]

	'''


	def sortList(self, li:list[int]) -> list:
		for i in range(len(li)):
			for j in range(len(li) - i - 1):
				if li[j] > li[j + 1]:
					# swap like using pointers
					li[j], li[j + 1] = li[j + 1], li[j]
		return li
	

	def isContent(self, size:int, greed:int ) -> bool:
		''' s[j]>=g[i] --> cookie_size >= kid_greed '''
		return size >= greed




	'''
	child recieve max 1 cookie.
	g[i]: minimum cookie size
	j: cookie
	s[j]: cookie size

	if s[j]>=g[i]: i can recieve j 

	GOAL: MAXIMIZE AMOUNT OF CONTENT CHILDREN
	'''



#* ACCEPTED; CLEAN VERSION
class Solution:
	def findContentChildren(self, g: list[int], s: list[int]) -> int:
		s.sort(), g.sort()
		content_counter,i,y = 0,0,0
		while i < len(s):
			if y == len(g): break
			if s[i] >= g[y]:
				y+=1; content_counter+=1
			i+=1
		return content_counter


if __name__ == '__main__':

	cases = [
		[10,2,222,4,1,10],	# g
		[6,100,1,2,3,6],			# s	
	
		# [1,2],				# g
		# [1,2,3],			# s

		# [1],                # g (length >= 1)
		# [],                 # s (length >= 0)

		# [2147483647],       # g (max value allowed)
		# [2,3],             # s (valid, length >= 0)

		# [123,456,789],    # g
		# [7],                # s

		# [999999999,42],    # g
		# [2147483647,1,5]  # s
	]

	for i in range(0, len(cases), 2):  # step of 2
		g, s = cases[i], cases[i+1]
		sol = Solution()
		print(f"___ NO.{i} ___________________________________")
		sol.findContentChildren(g,s)
		# print(f"n={i} -> {sol.findContentChildren(g,s)}")
		print("\n")


# [1]                
# []                 
# [2147483647]       
# [2, 3]             
# [123, 456, 789]    
# [7]                
# [999999999, 42]    
# [2147483647, 1, 5]  