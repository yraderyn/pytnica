import re
niskapogrešnih = str()
listasufiksa = ['ac', 'aš', 'nik', 'anin', 'ka', 'ica', 'je', 'će', 'đe', 'stvo', 'ina', 'ba', 'ov', 'oš', 'ost', 'er', 'ić', 'njak', 'izam', 'ija', 'ika', 'telj', 'ina', 'aj', 'tura', 'ač', ]
listaprefiksa = ['protiv', 'nadri', 'preda', 'nada', 'poda', 'beza', 'raza', 'polu', 'pred', 'pret', 'vele', 'samo', 'mimo', 'među', 'bez', 'bes', 'bež', 'beš', 'van', 'pod', 'pot', 'pra', 'pre', 'pro', 'pri', 'raz', 'ras', 'raž', 'raš', 'nad', 'nat', 'naj', 'nuz', 'nus', 'oda', 'iza', 'oba', 'op', 'pa', 'po', 'do', 'is', 'iž', 'iš', 'uz', 'us', 'už', 'uš', 'na', 'ne', 'su', 'sa', 'od', 'ot', 'ob', 'za', 'iz', 'o', 'u', 's', 'z']
with open("reizlaz2.txt", "r", encoding="utf-8") as Ulaz:
	lista = [red[:-1] for red in Ulaz.readlines()]
	niska = ' '.join(lista)
	with open("3dobro.txt", "w", encoding="utf-8") as Izlaz:
		with open("3loše.txt", "w", encoding="utf-8") as Pogrešan:
			with open("3sufiksi.txt", "w", encoding="utf-8") as Sufiksi:
				for reč in lista:
					zapisana = False
					for prefiks in listaprefiksa:
						### NALAZI REČI KOJE IMAJU PREFIKS ###
						nađen = re.match(prefiks, reč)
						if nađen:
							izbaci = prefiks+" "+reč
							for prefiks2 in listaprefiksa:
								if prefiks != prefiks2:
									#if zapisana == True:
										#break
									### PROVERAVA IMA LI DVA PREFIKSA ###
									if reč[len(prefiks):].startswith(prefiks2) and reč[(len(prefiks) + len(prefiks2)):] != "" and prefiks + prefiks2 not in listaprefiksa and len(prefiks) + len(prefiks2) > 2:
										izbaci2 = prefiks + ' ' + prefiks2 + ' ' + reč
										### REČ BEZ PREFIKSÂ NELEKSIKALIZOVANA ###
										for prefiks3 in listaprefiksa:
											if prefiks2 != prefiks3 and reč[(len(prefiks) + len(prefiks2)):]!="":
												#print(prefiks3 + ' ' + prefiks)
												recy = re.findall(" " + prefiks3 + reč[(len(prefiks) + len(prefiks2)):] + " ", niska)
												#print(str(reč) + ' ' + str(recy))
												if recy:
													Izlaz.write(izbaci2 + ' - nađeno jer ima DVA PREFIKSA NA NELEKSIKALIZOVANOJ\n')
													zapisana = True
													break
												elif izbaci not in niskapogrešnih:
													niskapogrešnih = niskapogrešnih + izbaci + " - ŠLJBLJMEHEHEHEHEHEHEHX\n"
										### REČ BEZ PREFIKSÂ LEKSIKALIZOVANA ###
										if ' ' + reč[(len(prefiks) + len(prefiks2)):] + ' ' in niska and zapisana == False:
											Izlaz.write(izbaci2 + ' - nađeno jer ima DVA PREFIKSA\n')
											zapisana = True
											break
									### PROVERAVA IMA LI ISTE OSNOVE SA DRUGIM PREFIKSOM ###
									elif reč[len(prefiks):]!="" and zapisana == False:
										#print(prefiks2 + ' ' + prefiks)
										rec = re.findall(" " + prefiks2 + reč[len(prefiks):] + " ", niska)
										#print(str(reč) + ' ' + str(rec))
										if rec:
											Izlaz.write(izbaci + ' - nađeno jer se prefiks može ZAMENITI drugim prefiksom\n')
											zapisana = True
											#break
										'''elif izbaci not in niskapogrešnih:
											niskapogrešnih = niskapogrešnih + izbaci + "\n"'''
									else:
										pass
							### TRAŽI REČI KOJIH JE OSNOVA LEKSIKALIZOVANA ###
							if ' ' + reč[len(prefiks):] + ' ' in niska and zapisana == False:
								Izlaz.write(izbaci + ' - nađeno jer je ostatak reči U KORPUSU\n')
								zapisana = True
							if zapisana == False:
								for sufiks in listasufiksa:
									if reč.endswith(sufiks) and zapisana == False:
										Sufiksi.write(reč + "\n")
										zapisana = True
									else:
										break
								if zapisana == False:
									Pogrešan.write(izbaci + "\n")