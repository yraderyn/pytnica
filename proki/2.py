### BRIŠE FREKVENCIJE ###
import re
with open("1.txt", "r", encoding="utf-8") as Ulaz:
	with open("2.txt", "w", encoding="utf-8") as Izlaz:
		for red in Ulaz:
			red = re.sub(", ",'', red)
			red = re.sub("\d",'', red)
			Izlaz.write(red)