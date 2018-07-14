recnik = dict()
import re
import string

### DEO KOJI BIRA ###
with open("korpus.txt", "r", encoding="utf-8") as Korpus:
	for starired in Korpus:
		try:
			reci = starired.split('\t')
			if (reci[6].startswith("N")) and (reci[7][0].isupper() == False): # proverava je li imenica i ima li velikih slova
				try:
					recnik[reci[7]] += 1
				except:                       # ovde meri frekvenciju
					recnik[reci[7]] = 1
		except:
			pass

### DEO KOJI SORTIRA PO ABECEDI ###
sorted_by_value = sorted(recnik.items(), key=lambda kv: kv[1])

### DEO KOJI ZAPISUJE ###
with open("1.txt", "w", encoding="utf-8") as Sortirano:
	for x in sorted_by_value:
		red = str(x)
		red = re.sub("\(",'', red)
		red = re.sub("\)",'', red)
		red = re.sub("'",'', red)
		red = re.sub(r'\\n','', red)
		red = re.sub("nx",'nj', red)
		red = re.sub("zx",'ž', red)
		red = re.sub("sx",'š', red)
		red = re.sub("dx",'đ', red)
		red = re.sub("dy",'dž', red)
		red = re.sub("cy",'č', red)
		red = re.sub("cx",'ć', red)
		red = re.sub("lx",'lj', red)
		Sortirano.write(red + "\n")
