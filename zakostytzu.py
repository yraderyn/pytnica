import re
niskapogrešnih = str()
listaprefiksa = ['protivu', 'protiv', 'nadri', 'preda', 'nada', 'poda', 'beza', 'raza', 'polu', 'pred', 'pret', 'vele', 'samo', 'mimo', 'među', 'bez', 'bes', 'bež', 'beš', 'van', 'pod', 'pot', 'pra', 'pre', 'pri', 'raz', 'ras', 'raž', 'raš', 'nad', 'nat', 'naj', 'nuz', 'nus', 'oda', 'iza', 'oba', 'pa', 'po', 'do', 'iz', 'is', 'iž', 'iš', 'uz', 'us', 'už', 'uš', 'na', 'ne', 'su', 'sa', 'od', 'ot', 'ob', 'o', 'u', 's', 'z']
with open("2.txt", "r", encoding="utf-8") as Ulaz:
	lista = [red[:-1] for red in Ulaz.readlines()]
	niska = ' '.join(lista)
	with open("3dobro.txt", "w", encoding="utf-8") as Izlaz:
		with open("3loše.txt", "w", encoding="utf-8") as Pogrešan:
			for reč in lista:
				for prefiks in listaprefiksa:
					nađen = re.match(prefiks, reč)
					if nađen:
						for prefiks2 in listaprefiksa:
							if prefiks2 != prefiks and reč[len(prefiks):]!="":
								print(prefiks2 + ' ' + prefiks)
								rec = re.findall(" " + prefiks2 + reč[len(prefiks):] + " ", niska)
								print(str(reč) + ' ' + str(rec))
								izbaci=prefiks+" "+reč
								if rec:
									Izlaz.write(izbaci + '\n')
									break
								elif izbaci not in niskapogrešnih:
									niskapogrešnih = niskapogrešnih + izbaci + "\n"
							else:
								pass
			Pogrešan.write(niskapogrešnih)
