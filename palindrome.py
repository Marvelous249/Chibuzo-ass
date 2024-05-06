def is_Palindrome(word):
	reversed_word = ""
 	for index in range(len(word)-1, -1, -1):
		reversed_word += wore[index]
	return word == reversed_word
