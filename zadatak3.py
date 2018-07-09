devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima"
lista_stihova = devojka_iz_petnice.split('\n')
konacna = list()
for stih in lista_stihova:
	reciustihu = stih.split(' ')
	for rec in reciustihu:
		konacna.append(rec)
	reciustihu = list()
k2 = list()
for a in konacna:
	if a == "Devojke":
		a = "Dečaci"
	if a == "Devojka":
		a = "Dečak"
	if a == "joj":
		a = "mu"
	if a == "mrtvi":
		a = "mrtva"
	if a == "Mrtvi":
		a = "Mrtva"
	if a == "pisac":
		a = "spisateljica"
	if a == "njenim":
		a = "njegovim"
	if a == "koju":
		a = "kojeg"
	if a == "ona":
		a = "on"
	if a.endswith("io") == True:
		a = a.replace("io","ila")
	if a.endswith("eo") == True:
		a = a.replace("eo","ela")
	if (a.endswith("ac") == True) and (a != "pisac"):
		a = a.replace("ac","ka")
	if a.endswith("an") == True:
		a = a.replace("an","na")
	else:
		if a.endswith("na") == True:
			a = a.replace("na","an")
	if a.endswith("en") == True:
		a = a.replace("en","ena")		
	k2.append(a)
print(k2)
