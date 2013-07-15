#Dev-Sprint5, Ch12 (Tuples)
#Name: Lisa=Maria Mehta

# *************************************
# ** Exercise 12.4 -- More anagrams! **
# *************************************
# Starting out: Building an anagram dictionary
#---------------------------------------------


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to getting and searching for words, ++++++
#                             Taken from 'Think Python' ++++++ 
#                                                    +++++++++ 
def make_word_list(fin):
	""" 
	Taken from 'Think Python.' Reads lines from a file 
	and builds a list using append.
	"""
	word_list = []
	for line in fin:
		word = line.strip()
		word_list.append(word)
	return word_list

def in_bisect(word_list, word):
	"""
	Taken from 'Think Python.'Checks whether a word is 
	in a list using bisection search.
	Precondition: the words in the list are sorted
	word_list: list of strings
	word: string
	"""
	i = bisect_left(word_list, word)
	if i != len(word_list) and word_list[i] == word:
		return True
	else:
		return False
#                                                    +++++++++ 
# End Functions related to getting and searching for words +++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to forming anagram dictionary ++++++++++++
#                                                +++++++++++++ 
def get_sorted_anagram(word):
	'''Takes a str (word) as an argument, and returns a string
	with the letters of the word in alphabetical order. 
	For example 'word' becomes 'dorw', and
	'mouse' becomes 'emosu'.'''
	temp=list(word)
	temp.sort()
	sorted_string = ''
	for letter in temp:
		sorted_string += str(letter)
	return sorted_string

def make_wordpair(word):
	'''
	Takes a str (word) as an argument.  Calls on 
	get_sorted_anagram, and returns a tuple with 
	both the new (alphabetical) string, and the original word. 
	'''
	sorted_string = get_sorted_anagram(word)
	return sorted_string, word

def build_wordpairs_list(wordlist):
	'''
	Takes a list of strings as an argument. Calls make_wordpair
	for each string, and builds a new list (word_pairs_list) 
	using the results.  Skips strings of length 1.
	Returns the sorted word_pairs_list.
	'''
	wordpairs_list=list()
	for i in range(len(wordlist)): #loop to see every element
		if len(wordlist[i])>1: # only adds "words" of >1 char
			wordpairs_list.append(make_wordpair(wordlist[i]))
	return (sorted(wordpairs_list))
	
def build_dict(sorted_wordpairs_list):
	'''
	Takes a list of lists as an argument, and returns a dictionary.
	Uses the first element of the individual lists as the Key.  All 
	lists with the same first element are combined.  The function 
	returns a dictionary (anagram_dict) using the alphabetical 
	sorted anagram as the key, and a list of all 
	meaningful anagrams as the value (while skipping words with no
	meaningful anagrams.)
	'''
	anagram_dict= dict()
	oldkey = ''
	wordlist = []
	for i in range(len(sorted_wordpairs_list)):
		key =sorted_wordpairs_list[i][0] 
		if key != oldkey:
			wordlist = []
			wordlist.append(sorted_wordpairs_list[i][1])
		elif key == oldkey:
			wordlist.append(sorted_wordpairs_list[i][1])
			anagram_dict[key] = wordlist
		oldkey = key
	return anagram_dict
#                                                    +++++++++ 
# End functions related to getting and searching for words, ++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions related to output ++++++++++++++++++++++++++++++++
#                                                +++++++++++++ 
def print_dict(d):
	for key in d:
		print key, d[key]

def print_list(l):
	for i in range(len(l)):
		print l[i] 
#                                                    +++++++++ 
# End functions related to output ++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# *********************
# ** Exercise 12.4.1 **
# *********************
# Do elements in a wordlist have anagrams?
# ----------------------------------------
def get_anagrams (word, anagram_dict):
	'''
	Takes a str and dictionary as argument.
	Using the str as a key, returns the value in the dictionary.
	Returns None if key is not found.
	'''
	key = get_sorted_anagram(word)
	if key in anagram_dict:
		return anagram_dict[key]
	else:
		return None

#def build_anagrams_list(testlist, anagrams_list):
#	anagrams_list = []
#	for word in testlist:

def build_anagrams_list(testlist, anagram_dict):
	'''
	Adapted from Think Python.
	Takes a list of strings and a dictionary as arguments.
	For each string in the list, finds the corresponding
	value in the dictionary, if any. 
	Returns a list of lists of anagrams.
	'''
	t = []
	for word in testlist:
		list = get_anagrams(word, anagram_dict)
		if list != None:
			t.append(list)
	return t


# *********************
# ** Exercise 12.4.2 **
# *********************
# Which word has more anagrams?
# -----------------------------

def sort_by_length (anagrams_list):
	'''
	Adapted from Think Python.  Takes an anagram list as
	an argument, and returns a list of tuples with
	the length of they tuple, and the anagram words list.
	'''
	t = []
	for element in anagrams_list:
		t.append((len(element), element))
	t.sort(reverse = True)
	res = []
	for num, element in t:
		res.append(element)
	return res

# *********************
# ** Exercise 12.4.3 **
# *********************
# Eight-letter words with anagrams
# --------------------------------

def find_eight_letter_anagrams(anagram_dict):
	'''
	Takes an anagram_dict as an argument, and
	returns the largest anagram list with
	eight-letter elements.
	'''
	eights_list = []
	for key in anagram_dict:
		if len(key) == 8:
			eights_list.append((len(anagram_dict[key]), anagram_dict[key]))
	eights_list.sort(reverse = True)
	return eights_list[0][1]









# Main Program
# ------------
textfile = 'words.txt'
testwordfile = 'testlist.txt'
fin1 = open(textfile)
fin2 = open(testwordfile)
wordlist = make_word_list(fin1)
testlist = make_word_list(fin2)

sorted_wordpairs_list = build_wordpairs_list(wordlist)
anagram_dict = build_dict(sorted_wordpairs_list)

print
print "List of test words for exercises"
print "--------------------------------"
print testlist

print
print "Exercise 12.4.1: Anagrams for words in a test file"
print "--------------------------------------------------"
ang_list = build_anagrams_list(testlist, anagram_dict)
print_list(ang_list)


print
print "Exercise 12.4.2: Same list, but in descending order"
print "                              of number of elements"
print "---------------------------------------------------"
sorted_ang_list = sort_by_length(ang_list)
print_list(sorted_ang_list)

print
print "Exercise 12.4.3: Best Scrabble 'Bingo' words"
print "--------------------------------------------"
best_bingo_words = find_eight_letter_anagrams(anagram_dict)
print_list (best_bingo_words)