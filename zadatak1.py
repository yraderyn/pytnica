devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
aa = devojka_iz_petnice.lower()
lista_stihova = aa.split('\n')
konacna = list()
for stih in lista_stihova:
	reciustihu = stih.split(' ')
	for rec in reciustihu:
		if rec != '':
			rec = rec.strip("?")
			konacna.append(rec)
	reciustihu = list()
print(len(konacna))
# prva varijanta:
neponovljene = list()
for i in konacna:
	if i not in neponovljene:
		neponovljene.append(i)
# druga varijanta:
# neponovljene = set(y)
print(len(neponovljene))
