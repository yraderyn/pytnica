with open("../izlaz.txt", "r", encoding="utf-8") as izlaz:
	lista = list()
	import re
	for rec in izlaz:
		tmp = re.match("š|đ|č|ć|ž|[a-z]", rec) 
		if tmp != []:
			lista.append(rec)
with open("reizlaz.txt", "w", encoding="utf-8") as reizlaz:
	for element in lista:
		reizlaz.write(element)