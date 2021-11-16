from counter import count_words_fast
from read_book import Read_book

def word_stats(word_counts):
	num_words=len(word_counts)
	counts=word_counts.values()
	return (num_words, counts)

#print(word_stats(count_words_fast(Read_book("./Libros/Romeo and Juliet (guion).txt"))))
