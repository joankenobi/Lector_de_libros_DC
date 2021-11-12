def read_book(book_title_path):
	book=book_title_path
	with open(book, "r") as open_book:
		text_book=open_book.read()
	text_book=text_book.replace("\n"," ").replace("\r","")
	return text_book

text=read_book("./Libros/Romeo and Juliet (guion).txt")
ind=text.find("Good morrow, cousin.")
print(text[ind:ind +100])