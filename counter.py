def counter_word(text:str):
	text=text.split(" ")
	counted_words={} 
	for word in text:
		#know words
		if word in counted_words:
			counted_words[word]+=1
		#Unknow words
		else:
			counted_words[word]=1
	return counted_words

text="joan joel josue joan"
print(counter_word(text))
