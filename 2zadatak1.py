lista = list()
with open("nusic-svet.txt", "r", encoding="utf-8") as Nusic:
	for red in Nusic:
		print(red.strip("\n"))
		reciuredu = red.split(" ")
		for rec in reciuredu:
			lista.append(rec.replace("\n", ""))
	g = "\n".join(lista)
	with open("izlaz.txt", "a+", encoding="utf-8") as Izlaz:
		Izlaz.write(g)
	print(g)
