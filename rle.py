# Examples
# "AAAAACCCCDDDDSTTT" 5A4C4DS3T
# "AABCCD" cannot compress further
# "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW" 12WB12W3B24WB14W

def encode(string):
	count = 1
	char = string[0]
	new = ""
	start = 0

	pos = 0
	while pos < len(string): # just iterating through the string but giving us control over the position
		if pos < len(string)-1: # are we before the last char of the string
			if string[pos+1] == char: # is the next char the same as the current run's char
				count += 1
			else: # we are on a new run
				# check if the previous run was 3 or more
				# no point converting AA to 2A nor A to 1A
				if count > 2:
					new += str(count) + char
				else:
					new += char * count
				char = string[pos+1] # set current run's character to char ahead
				count = 1
		else: # we are at the end character
			if count > 2:
				new += str(count) + char
			else:
				new += char * count
		pos += 1 # move onto the next character
	return new

def decode(string):
	new = ""
	count = ""
	pos = 0
	while pos < len(string): # just iterating through the string but giving us control over the position
		if pos < len(string)-1: # are we before the end of the string
			if string[pos].isdigit(): # is the current char a number
				count += string[pos] # append to the string the number
			else: # the char is not a digit
				new += string[pos] # just append the char to the string
			if not string[pos+1].isdigit(): # if the next char is not a digit
				if count != "": # if count = "" then there isnt a count
					new += string[pos+1] * int(count) # append the char as many times as the count
					count = ""
					pos += 1 # move an extra position along since we have already handled the next char
		else: # we are on the last char
			new += string[pos] # just add the char as it has not been handled already meaning no count
		pos += 1
	return new


# Example string and encoded counter part taken from wikipedia
wiki = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
wikiEncoded = "12W1B12W3B24W1B14W"
encoded = encode(wiki)
decoded = decode(wikiEncoded)
print("Sample string:", wiki)
print("Encoded example:", wikiEncoded)
print("Encoded string:", encoded)
print("Is decoded the same?", decoded == wiki)
