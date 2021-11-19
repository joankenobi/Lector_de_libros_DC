import matplotlib.pyplot as plt
from archive_admin import admin_dir

#def graficando(tabla):
	#grafica=plt.plot(tabla.Length, tabla.Unique, "bo")
	#grafica=plt.loglog(tabla.Length, tabla.Unique, "bo")
	#return plt.savefig("la graph2.pdf")

book_dir="./Libros"
tabla= admin_dir(book_dir)
#graf_ingles=graficando(tabla)
#graf=graficando(tabla)
#graf.savefig("la grafica.pdf")

#plt.figure(figsize=(10,10))
subset=tabla[tabla.Language=="Ingles"]
plt.loglog(subset["Length"], subset.Unique, "o", label="Ingles", color="blue")

subset=tabla[tabla.Language=="Portugues"]
plt.loglog(subset.Length, subset.Unique, "o", label="Portugues", color="green")

subset=tabla[tabla.Language=="Aleman"]
plt.loglog(subset.Length, subset.Unique, "o", label="Aleman", color="crimson")

plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number unique")
plt.savefig("la graph3.pdf")