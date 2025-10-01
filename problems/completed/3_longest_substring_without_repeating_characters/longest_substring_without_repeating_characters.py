''' * 3. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
		
		Given a string s, find the length of the longest substring without repeating characters.

		Example 1:
				Input: s = "abcabcbb"
				Output: 3
				Explanation: The answer is "abc", with the length of 3.

		Tolkning:
			maskinen bygger en substring ut av en string, hvor den legger til ["i" for i in String] = substring.
			Når et tegn som har blitt tidligere nevnt blir nevnt igjen, slutter maskingen å legge til flere tegn til substringen.
			Når den har møtt på et tegn som er gjentatt, starter den på nytt igjen fra det gjentatte tegnet;
			
			start 	  	Stop (gjentagelse)			ny start 		 start 							<-- event
			 |					|						|			   |							<-- event-punkt
			"Abcabcd" 		"abcAbcd"				"abcAbcd"		"..Abcd"						<-- String
							["a","b","c"] => "abc"		     		["a","b","c","d"] => "abcd"		<-- substrings funnet 	
			
			
			Så skal den gå igjennom alle substringene, og finne den lengste;
			
			longest_substring = ""
			for i in substrigs: --> "for str in (list[str])"
				try:
					if len(i) > len(i+1) 
						longest_substring = i
				except InderError:
					return longest_substring


			i "abca" er "abc" riktig fordi, den andre "a" ("abcA" ) er allerede blitt nevnt ("Abca"), 
			dermed stopper telleren, og slutter å legge til flere karakterer til substringen. 

			Hensyn:
				koden må sørge for at alle characters er i lowercase.
			
			Constraints:	
				String skal bestå av:
					- English letters, digits, symbols and spaces.
				? jeg antar at symboler, tall og mellomrom teller som gyldige tegn
'''


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		maxLength = 0
		currentSubstring = ""
		for x in s:
			if x in currentSubstring:
				currentSubstring = currentSubstring[currentSubstring.rfind(x)+1:]+x
			else:
				currentSubstring += x
				maxLength = max(len(currentSubstring), maxLength)
		return maxLength



class Input:
	def getInputs(self):
			return [ 
					# "abcb",
					# "abcabcbb", 
					# "bbbbb",
					"pwwkew",
					# "",
					# " ",
					# "au",
					# "i",
					# "1",
					# "dvdf",
					# "anviaj",
					]


def main():
	I = Input()
	S = Solution()
	for input_ in I.getInputs():
		# print(input_)
		result = S.lengthOfLongestSubstring(input_)
		print(result)
		# print("="*20)
		# print(f"RESULT = {result}")

if __name__ == '__main__':
	main()


