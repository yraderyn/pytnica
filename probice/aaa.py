str = "aaa fjr aaa aaa ofor vekfe pj pj dgjelv pj rgpn pe sfvj sfvj sfvj jrvpej sfvj j"
lista = str.split(" ")
recnik = { n : lista.count(n) for n in lista }
print(sorted(recnik))