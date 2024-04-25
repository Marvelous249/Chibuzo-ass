from corn_flakes import length_characters
from corn_flakes import add_ing
from corn_flakes import longest_word
from corn_flakes import odd_index

def test_length_characters():
	assert length_characters ('semicolon') == 'seon'
	assert length_characters ('on') == 'onon'
	assert length_characters ('o') == " "

def test_add_ing():
	assert add_ing('on') == 'on'
	assert add_ing('abc') == 'abcing'
	assert add_ing('String') == 'Stringily'

def test_longest_word():
	words = ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']
	longest, length = longest_word(words)
	assert longest == 'breakfast' and length == 9

def test_odd_index():
	word = "semicolon"
	assert odd_index(word) == 'eioo'

