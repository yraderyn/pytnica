niska = "loshmi ye kupował razorrassy nerazya ya cvou necectricxyny"
prefiks1 = "ne"
prefiks2 = "raz"
lista = niska.split( )
for x in lista:
	if prefiks1 + prefiks2 + x[(len(prefiks1) + len(prefiks2)):] in niska and x[(len(prefiks1) + len(prefiks2)):] != "" and ' ' + x[(len(prefiks1) + len(prefiks2)):] + ' ' in niska:
		print(prefiks1 + prefiks2 + x[(len(prefiks1) + len(prefiks2)):])
		print(x + " ovo je x")