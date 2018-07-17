### THE MAIN DEAL ###
import re
niskapogrešnih = str()
listasufiksa = ['ac', 'aš', 'nik', 'anin', 'ka', 'ica', 'je', 'će', 'đe', 'stvo', 'ina', 'ba', 'ov', 'oš', 'ost', 'er', 'ić', 'njak', 'izam', 'ija', 'ika', 'telj', 'ina', 'aj', 'tura', 'ač', ]
listaprefiksa = ['protivu', 'protiv', 'nadri', 'preda', 'nada', 'poda', 'beza', 'raza', 'polu', 'pred', 'pret', 'vele', 'samo', 'mimo', 'među', 'bez', 'bes', 'bež', 'beš', 'van', 'pod', 'pot', 'pra', 'pre', 'pro', 'pri', 'raz', 'ras', 'raž', 'raš', 'nad', 'nat', 'naj', 'nuz', 'nus', 'oda', 'iza', 'oba', 'pa', 'po', 'do', 'iz', 'is', 'iž', 'iš', 'uz', 'us', 'už', 'uš', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ot', 'ob', 'o', 'u', 's', 'z']
with open("reizlaz2.txt", "r", encoding="utf-8") as Ulaz:
	lista = [red[:-1] for red in Ulaz.readlines()]
	niska = ' '.join(lista)
	with open("3dobro.txt", "w", encoding="utf-8") as Izlaz: # ove reči je program prepoznao kao reči sa prefiksom i zadovoljavaju neki od uslova
		with open("3loše.txt", "w", encoding="utf-8") as Pogrešan: # ove reči program nije prepoznao kao reči, ali je našao prefiks
			with open("3sufiksi.txt", "w", encoding="utf-8") as Sufiksi: # ove reči program takođe nije prepoznao kao reči, ali imaju i prefiks i sufiks, što ih čini verovatnijima da su zapravo reči
				for reč in lista:
					zapisana = False
					for prefiks in listaprefiksa:
						### NALAZI REČI KOJE IMAJU PREFIKS; SVE POSLE OVOGA SE TIČE REČI KOD KOJIH JE NAŠAO PREFIKS ###
						nađen = re.match(prefiks, reč)
						if nađen:
							izbaci = prefiks+" "+reč
							for prefiks2 in listaprefiksa:
								if prefiks != prefiks2:
									if zapisana == True:
										break
									### PROVERAVA IMA LI DVA PREFIKSA ###
									if reč[len(prefiks):].startswith(prefiks2) and reč[(len(prefiks) + len(prefiks2)):] != "" and prefiks + prefiks2 not in listaprefiksa and len(prefiks) + len(prefiks2) > 2:
										izbaci2 = prefiks + ' ' + prefiks2 + ' ' + reč
										### AKO JE OSNOVA NELEKSIKALIZOVANA (sa dva prefiksa) ###
										for prefiks3 in listaprefiksa:
											if prefiks2 != prefiks3 and reč[(len(prefiks) + len(prefiks2)):]!="":
												recy = re.findall(" " + prefiks3 + reč[(len(prefiks) + len(prefiks2)):] + " ", niska)
												if recy:
													Izlaz.write(izbaci2 + ' - nađeno jer ima DVA PREFIKSA NA NELEKSIKALIZOVANOJ\n')
													zapisana = True
													break
										### AKO JE OSNOVA LEKSIKALIZOVANA (sa dva prefiksa) ###
										if ' ' + reč[(len(prefiks) + len(prefiks2)):] + ' ' in niska and zapisana == False:
											Izlaz.write(izbaci2 + ' - nađeno jer ima DVA PREFIKSA\n')
											zapisana = True
											break
									### PROVERAVA IMA LI ISTE OSNOVE REČI, ALI SA DRUGIM PREFIKSIMA ###
									elif reč[len(prefiks):]!="" and zapisana == False:
										rec = re.findall(" " + prefiks2 + reč[len(prefiks):] + " ", niska)
										if rec:
											Izlaz.write(izbaci + ' - nađeno jer se prefiks može ZAMENITI drugim prefiksom\n')
											zapisana = True
											break
									else:
										pass
							### TRAŽI REČI KOD KOJIH JE OSNOVA LEKSIKALIZOVANA ###
							if ' ' + reč[len(prefiks):] + ' ' in niska and zapisana == False:
								Izlaz.write(izbaci + ' - nađeno jer je ostatak reči U KORPUSU\n')
								zapisana = True
							### AKO NIŠTA OD OVOGA NIJE ISPUNJENO: ###
							if zapisana == False:
								### TRAŽI SUFIKS I TAKVE REČI IZBACUJE U POSEBNU LISTU ###
								for sufiks in listasufiksa:
									if reč.endswith(sufiks) and zapisana == False:
										Sufiksi.write(reč + "\n")
										zapisana = True
								### OVDE IZBACUJE REČI KOD KOJIH JE PREPOZNAO PREFIKS, ALI TO VEROVATNO NISU REČI NASTALE PREFIKSACIJOM JER NIJEDAN DRUGI USLOV NIJE ISPUNJEN ###
								if zapisana == False:
									Pogrešan.write(izbaci + "\n")