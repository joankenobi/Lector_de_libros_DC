from collections import Counter


def counter_word(text:str):
	miss=[":",".",";",",","'",'"']
	for special_elem in miss:
		text=text.replace(special_elem,"")
	text=text.lower().split(" ")
	counted_words=Counter(text)
	#counted_words={} 
	#for word in text:
	#	#know words
	#	if word in counted_words:
	#		counted_words[word]+=1
	#	#Unknow words
	#	else:
	#		counted_words[word]=1
	return counted_words

text="This is my text text. we're keeping this text short to keep things manageable."
print(counter_word(text))
