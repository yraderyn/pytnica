with open('reizlaz2.txt', 'r', encoding = 'utf-8') as korpus:
    recnik = [red[:-1] for red in korpus.readlines()]
    listaprefiksa = ['protivu', 'protiv', 'preda', 'nada', 'poda', 'beza', 'raza', 'polu', 'pred', 'pret', 'samo', 'mimo', 'među', 'bez', 'bes', 'bež', 'beš', 'van', 'pod', 'pot', 'pra', 'pre', 'pro', 'pri', 'raz', 'ras', 'raž', 'raš', 'nad', 'nat', 'naj', 'nuz', 'nus', 'oda', 'iza', 'oba', 'po', 'do', 'iz', 'is', 'iž', 'iš', 'uz', 'us', 'už', 'uš', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ot', 'ob', 'o', 'u', 's', 'z']
    listasufiksa = ['je', 'đe', 'će', 'lje', 'nje', 'aš', 'nik', 'ac', 'ar', 'ak', 'ica', 'ina', 'inja', 'če', 'anj', 'njak', 'ija', 'ište', 'aj', 'enje', 'im', 'ima', 'stvo', 'uša', 'ušan', 'anin', 'anka', 'izam', 'ista', 'istkinja', 'istica', 'ost', 'nost', 'a', 'telj', 'ba']
    prefiksi = list()
    sufiksi = list()
    def prefiksator(rec):
        for prefiks in listaprefiksa:
            if rec.startswith(prefiks):
                if len(rec[len(prefiks):]) < 2 or rec in listasufiksa or rec in listaprefiksa:
                        prefiksi.clear()
                        sufiksi.clear()
                        break
                if rec[len(prefiks):] in recnik:
                    prefiksi.append(prefiks)
                    rec = rec[len(prefiks):]
                    prefiksator(rec)
                    return prefiksi
                else:
                    for sufiks in listasufiksa:
                            if rec.endswith(sufiks):
                                prefiksi.append(prefiks)
                                sufiksi.append(sufiks)
                                return prefiksi, sufiksi
                                break
                    for prefiks2 in listaprefiksa:
                        if prefiks2 + rec[len(prefiks):] in recnik and prefiks != prefiks2:
                            prefiksi.append(prefiks)
                            break
                        else:
                            pass
            else:
                pass
    with open('3novo.txt', 'w', encoding = 'utf-8') as izlaz:
        with open('3novisufiksi.txt', 'w', encoding = 'utf-8') as novisufiksi:
            for rec in recnik:
                prefiksator(rec)
                if prefiksi != []:
                    if sufiksi == []:
                        izlaz.write(rec + ' : ' + str(prefiksi) + '\n')
                        prefiksi.clear()
                    else:
                        novisufiksi.write(rec + ' : ' + str(prefiksi) + ' : ' + str(sufiksi) + '\n')
                        prefiksi.clear()
                        sufiksi.clear()