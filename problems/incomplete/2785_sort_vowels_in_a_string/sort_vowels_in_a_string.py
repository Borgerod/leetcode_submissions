'''
RUNTIME:
my benchmark: 2979ms
	min.goal: 86ms
	mid.goal: 51ms
	max.goal: 17ms
'''
class Solution:
	def sortVowels(self, s: str) -> str:
		t:list = [] #premuted string (lists)
		code:list = [] #premuted string (lists)
		i = 0
		og_index = []
		c_index = []
		s=list(s)
		while i < len(s):
			if self.checkIfConsonant(s[i]): #standing for consonant-checker
				i+=1
				continue
			_i=len(code)
			added = False
			c = self.asciiConverter(s[i])
			while _i > 0:
				if not added:
					og_index.append(i)
					c_index.append(i)
					code.append(c)
					added = True
					
				if c >= code[_i-1]:
					_i=0 # break
					break
				
				elif c < code[_i-1]:
					# Remove the element we just added since we need to insert it at the correct position
					code.pop()
					c_index.pop()
					
					# Find the correct insertion position
					insert_pos = _i - 1
					while insert_pos > 0 and c < code[insert_pos - 1]:
						insert_pos -= 1
					
					# Get the position we need to swap with BEFORE inserting
					if insert_pos < len(c_index):
						target_pos = c_index[insert_pos]
					else:
						target_pos = i
					
					# Insert at the correct position
					code.insert(insert_pos, c)
					c_index.insert(insert_pos, i)
					
					# Perform the swap if needed
					if target_pos != i:
						s[i], s[target_pos] = s[target_pos], s[i]
						# Update the c_index to reflect the swap - the target position now has our character
						for j in range(len(c_index)):
							if c_index[j] == target_pos:
								c_index[j] = i
					
					break
			if len(code)==0:
				c_index.append(i)
				og_index.append(i)
				code.append(c)
			i+=1

		return "".join(s)













		print(f" t: 		{t}")
		return "".join(t)
	
	def asciiConverter(self, char:str, reverse:bool=False ) -> str:
		if reverse:
			return chr(int(char))
		return str(ord(char)).zfill(3) 


	def checkIfVowel(self, char) -> bool:
		return char.lower() in 'aeiou'

	def checkIfConsonant(self, char) -> bool:
		return not char.lower() in 'aeiou'
	
# class Solution:
# 	def sortVowels(self, s: str) -> str:
# 		t:list = [] #premuted string (lists)
# 		codes:list = [] #premuted string (lists)
# 		# s_ind = []

# 		i = 0
# 		while i < len(s): #>STEP 1: seperate vowels + convert to ascii
# 			if self.checkIfVowel(s[i]): 
# 				ascii = self.asciiConverter(s[i])
# 				t.append("*")
# 				codes.append(ascii)
# 			else:
# 				# s_ind.append(i)
# 				t.append(s[i])
# 			i+=1

# 		codes.sort() #>STEP 2: sort

# 		i = 0
# 		while i < len(t) and codes: #>STEP 3: convert back + merge
# 			if t[i]=="*":				
# 				t[i]=self.asciiConverter(codes[0], reverse=True)
# 				codes.pop(0)
# 			i+=1
# 		print(f" t: 		{t}")
# 		return "".join(t)
	
# 	def asciiConverter(self, char:str, reverse:bool=False ) -> str:
# 		if reverse:
# 			return chr(int(char))
# 		return str(ord(char)).zfill(3) 


# 	def checkIfVowel(self, char) -> bool:
# 		return char.lower() in 'aeiou'
	





# #! dropped, got too complex to be efficiant. started over with a simnpler soluton and took it from there.
# # uses the same asciiConverter & checkIfVowel as current model
# # class Solution:
# 	def sortVowels(self, s: str) -> str:
# 		s = s #0-indexed string
# 		i=0		
# 		t = "" #premuted string
# 		t:list = [] #premuted string (lists)
# 		codes:list = [] #premuted string (lists)
# 		code_ind = []
# 		s_ind = []
# 		vowels = []

# 		print(f" t: 		{t}")
# 		while i < len(s):
# 			# char = s[i]
# 			if self.checkIfVowel(s[i]): 
# 				vowels.append(s[i])
# 				ascii = self.asciiConverter(s[i])
# 				code_ind.append(i)
# 				if not codes:
# 					codes.append(ascii)
# 				else:
# 					# for code in codes:
# 					if ascii >= codes[-1]:
# 						print(f"	{ascii} >= {codes[-1]} (bigger):  {codes} <-- {ascii}")
# 						codes.append(ascii)
# 					elif ascii <= codes[0]:
# 						print(f"	{ascii} <= {codes[0]} (smaller): {ascii} --> {codes}")
# 						codes.insert(0, ascii)
# 					else:
# 						print(f"ERROR: {ascii} -X-> {codes}")
					

# 						# if ascii>=code:
# 						# 	codes.append(ascii); break
# 						# else:
# 						# 	codes.insert(0, ascii); break
# 			else:
# 				s_ind.append(i)
# 				t.append(s[i])
# 			char = "P"
# 			char = self.asciiConverter(*self.checkIfVowel(s[i]))
# 			t[i] = self.asciiConverter(*self.checkIfVowel(s[i]))
# 			t.append(self.asciiConverter(*self.checkIfVowel(s[i])))

# 			i+=1

		
# 		print(f"s_ind: {s_ind}, 		    t: {t}")
# 		print(f" vowels: {vowels}")
# 		print(f"code_ind: {code_ind}, 	codes: {codes}")
# 		t.sort()
		
# 		return "".join(t)
	
# 	def asciiConverter(self, char:str, reverse:bool=False ) -> str:
# 		if reverse:
# 			return chr(int(char))
# 		return str(ord(char)).zfill(3) 


# 	def checkIfVowel(self, char) -> bool:
# 		return char.lower() in 'aeiou'	

# 	# #! Dropped, has too high memory usage and runtime
# 	# @property
# 	# def asciiDict(self):
# 	# 	# for the lazy man
# 	# 	# for vowels only, might find a better way of doing this.
# 	# 	ascii_codes = {
# 	# 		'A': '065',
# 	# 		'E': '069',
# 	# 		'I': '073',
# 	# 		'O': '079',
# 	# 		'U': '085',
# 	# 		'a': '097',
# 	# 		'e': '101',
# 	# 		'i': '105',
# 	# 		'o': '111',
# 	# 		'u': '117',
# 	# 	}
# 	# 	return ascii_codes


if __name__ == '__main__':

	cases = [

		"lEetcOde",
		"lYmpH",
		"aBcDeFgHiJkLmNoPqRsTuVwXyZ",
		"HELLOworld",
		"PythonIsFun",
		"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
		"abcdefghijklmnopqrstuvwxyz",
		"QuickBrownFoxJumpsOverTheLazyDog",
		# "SortingVowelsIsInteresting",
		# "DataStructuresAndAlgorithms",
		# "OpenAIChatGPT",
		# "VisualStudioCode",
		# "MachineLearningRocks",
		# "GitHubCopilot",
		# "ProgrammingIsAwesome",
		# "UnitTestingIsImportant",
	]
	solution = Solution()
	for i, s in enumerate(cases):
		print(f"___ NO.{i} ___________________________________")
		print(f"n={i} -> {solution.sortVowels(s)}\n")
