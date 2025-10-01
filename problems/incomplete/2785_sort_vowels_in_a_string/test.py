def checkIfConsonant( char) -> bool:
	return not char.lower() in 'aeiou'
# s = "lEetcOde"
#original_order = [0,3,4,7]
s = "QuickBrownFoxJumpsOverTheLazyDog"
s=list(s)
# s  = [ #simplified for actual s 
# 'l', 'E', 'e', 't', 'c', 'O', 'D', 'e'
# ]

# _______________________
c_index = [
	# 0,
		   ]
code = [
	# '079',
]
og_index=[

]
i=0
print(f"	s: 	  {s}")
while i < len(s)-1:
	print(f"i:{i} | limit:{len(s)-1}")

	if checkIfConsonant(s[i]): #standing for asciiConverter
		print(f"	* found, skip\n")
		i+=1
		continue

	_i=len(code)
	added = False
	s[i]= str(ord(s[i])).zfill(3)
	while _i > 0:
		print(f"	i_:{_i} | limit:{len(code)}")
		print()
		if not added:
			og_index.append(i)
			c_index.append(i)
			code.append(s[i])
			added = True

		print(f"		s[i]:{s[i]} | code[_i]:{code[_i-1]}")
		print(f"		{s[i]} < {code[_i-1]} = {s[i] < code[_i-1]}")

		if s[i] >= code[_i-1]:
			_i=0 # break
			break
		elif s[i] < code[_i-1]:
			print(f"		** {s[i]}<{code[_i-2]} ")
			if s[i] < code[_i-2]:
				_i-=1
				c_index[_i], c_index[_i-1] = c_index[_i-1], c_index[_i]

			
			elif s[i] >= code[_i-2]:
				# Swap s[i] and s[c_index[_i-1]]
				swap_idx = c_index[_i-1]
				s[i], s[swap_idx] = s[swap_idx], s[i]
				_i -= 1


	if len(code)==0:
		c_index.append(i)
		og_index.append(i)
		code.append(s[i])
	print(f"	code: 	  {code}")
	print(f"	c_index:  {c_index}")
	print(f"	og_index: {og_index}\n")
	i+=1
	print(f"	s: 	  {s}")

print(f"s: {s}")