def length_characters (a):
	if len(a) < 2:
		return " "
	else:
		return a[:2] + a[ -2:]

def add_ing (a):
	if len(a) < 3:
		return a
	elif  a[-3:] == 'ing':
		return a + 'ily'
	else:
		return a + 'ing'

def longest_word (a ):
	longest = ' '
	length = 0
	for i in a:
		if len(i) > len(longest):
			longest = i
			length = len(i)
			
	return longest, length

def odd_index(word):
	new_word = ""
	for i in range(len(word)):
		if i % 2 != 0:
			new_word += word[i]

	return new_word
			