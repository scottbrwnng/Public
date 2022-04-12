# Input: User entered string
# Output: A substring that meets the following rules:
# • Print the longest possible substring
# • The substring cannot have any repeating characters
# • If there is a tie of the longest substring: Print the first
# • If the length of the longest substring is less than 3: Print  
#   too small to print.
#Example: 
#User enters the string character
#System responds with racte

# Python3 program to find and print longest
# substring without repeating characters.

# Function to find and print longest
# substring without repeating characters.
def findLongestSubstring(string):

	n = len(string)

	# starting point of current substring.
	start_point = 0

	# maximum length substring without
	# repeating characters.
	maxlen = 0

	# starting index of maximum
	# length substring.
	start_index = 0

	# Hash Map to store last occurrence
	# of each already visited character.
	pos = {}

	# Last occurrence of first
	# character is index 0
	pos[string[0]] = 0

	for i in range(1, n):

		# If this character is not present in hash,
		# then this is first occurrence of this
		# character, store this in hash.
		if string[i] not in pos:
			pos[string[i]] = i

		else:
			# If this character is present in hash then
			# this character has previous occurrence,
			# check if that occurrence is before or after
			# starting point of current substring.
			if pos[string[i]] >= start_point:

				# find length of current substring and
				# update maxlen and start accordingly.
				currlen = i - start_point
				if maxlen < currlen:
					maxlen = currlen
					start_index = start_point

				# Next substring will start after the last
				# occurrence of current character to avoid
				# its repetition.
				start_point = pos[string[i]] + 1
			
			# Update last occurrence of
			# current character.
			pos[string[i]] = i
		
	# Compare length of last substring with maxlen
	# and update maxlen and start accordingly.
	if maxlen < i - start_point:
		maxlen = i - start_point
		start_index = start_point
	
	# The required longest substring without
	# repeating characters is from string[start]
	# to string[start+maxlen-1].
	return string[start_index : start_index + maxlen]

    


# Driver Code
if __name__ == "__main__":

	string = input()
	print(findLongestSubstring(string))

# This code is contributed by Rituraj Jain
