import os
import pandas as pd
from counter import count_words_fast
from read_book import Read_book
from word_stats import word_stats

book_dir="./Libros"
def admin_dir(books_dir):
	
	stats= pd.DataFrame(columns= ("Language","Author","Title","Length","Unique"))
	title_num=1
	#print(os.listdir(book_dir))
	for language in os.listdir(book_dir):
		for author in os.listdir(book_dir + "/"+ language):
			for title in os.listdir(book_dir + "/"+ language + "/"+ author):
				inputfile = book_dir + "/" + language + "/"+ author + "/" + title
				#print(inputfile)
				text= Read_book(inputfile)
				(num_unique, counts)= word_stats(count_words_fast(text))
				#print(str(num_unique)+ " " + str(sum(counts)))
				stats.loc[title_num]=language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
				title_num += 1
	return stats

tabla=admin_dir(book_dir)

#print(tabla)
#print(tabla[tabla.Language=="Ingles"])


