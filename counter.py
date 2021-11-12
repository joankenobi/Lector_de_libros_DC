from collections import Counter


def count_words_fast(text:str):
	miss=[":",".",";",",","'",'"']
	for special_elem in miss:
		text=text.replace(special_elem,"")
	text=text.lower().split(" ")
	counted_words=Counter(text)
	return counted_words

def count_words(text:str):
	miss=[":",".",";",",","'",'"']
	for special_elem in miss:
		text=text.replace(special_elem,"")
	text=text.lower().split(" ")
	counted_words={} 
	for word in text:
		#know words
		if word in counted_words:
			counted_words[word]+=1
		#Unknow words
		else:
			counted_words[word]=1
	return counted_words

text="This is my text text. we're keeping this text short to keep things manageable."
print(count_words_fast(text) is count_words(text))
#print(len(count_words("This comprehension check is to check for comprehension.")))