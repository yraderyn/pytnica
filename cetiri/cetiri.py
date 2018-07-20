import re
with open('reizlaz2.txt', 'r', encoding = 'utf-8') as korpus:
    recnik = [red[:-1] for red in korpus.readlines()]
    listaprefiksa = ['protiv', 'raza', 'polu', 'pred', 'pret', 'samo', 'mimo', 'među', 'bez', 'bes', 'van', 'pod', 'pot', 'pra', 'pre', 'pri', 'raz', 'ras', 'raš', 'nad', 'nat', 'naj', 'nuz', 'nus', 'oda', 'po', 'do', 'iz', 'is', 'iž', 'iš', 'uz', 'us', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ot', 'ob', 'op', 'o', 'u', 's', 'z']
    listasufiksa = ['je', 'đe', 'će', 'lje', 'nje', 'aš', 'nik', 'ac', 'ar', 'ak', 'ica', 'ina', 'inja', 'če', 'anj', 'njak', 'ija', 'ište', 'aj', 'enje', 'im', 'ima', 'stvo', 'uša', 'ušan', 'anin', 'anka', 'izam', 'ista', 'istkinja', 'istica', 'ost', 'nost', 'a', 'telj', 'ba']
    listaprefiksasuslovima = ['is', 'us', 'ras', 'nus', 'bes', 'op', 'ot', 'pot', 'nat', 'pret', 'z', 'iš', 'raš', 'š', 'iž', 'ž', 'iza', 'raza', 'oda']
    listakulprefiksa = ['protiv', 'polu', 'pred', 'samo', 'mimo', 'među', 'bez', 'van', 'pod', 'pra', 'pre', 'pri', 'raz', 'nad', 'naj', 'nuz', 'po', 'do', 'iz', 'uz', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ob', 'o', 'u', 's']
    stip = ['is', 'us', 'ras', 'nus', 'bes', 'pret', 'ot', 'pot', 'nat', 'op']
    štip = ['iš', 'raš', 'š']
    žtip = ['iž', 'š']
    atip = ['iza', 'raza', 'oda']
    prefiksi = list()
    sufiksi = list()
    prefiks2 = ''

    def alomorf(prefiks):
        if prefiks in listaprefiksasuslovima:
            if prefiks in stip:
                a = re.match('[ptkhfcč]', rec[len(prefiks):])
                if a:
                    return True
            elif prefiks == 'z':
                a = re.match('[bdg]', rec[len(prefiks):])
                if a :
                    return True
            elif prefiks in štip:
                a = re.match('[čć]', rec[len(prefiks):])
                if a:
                    return True
            elif prefiks in žtip:
                a = re.match('[dž|đ]', rec[len(prefiks):])
                if a:
                    return True
            elif prefiks in atip:
                a = re.findall('[zbsš]', rec[len(prefiks):])
                if a:
                    return True
        elif prefiks in listakulprefiksa:
            return True
        else:
            return False

    def prefiksator(rec):
        
        for prefiks in listaprefiksa:
            if rec.startswith(prefiks) and alomorf(prefiks) == True:
                zap = False
                if len(rec[len(prefiks):]) < 2 or rec in listasufiksa or rec in listaprefiksa:
                    break
                for prefiks2 in listaprefiksa:
                    if alomorf(prefiks2) == True and prefiks2 != prefiks and zap == False:
                        if prefiks2 + rec[len(prefiks):] in recnik and rec[len(prefiks):] in recnik:
                            leksiprod.write(prefiks + ' (' + prefiks2 + ') : ' + rec + '\n')
                            zap = True
                            break
                        elif prefiks2 + rec[len(prefiks):] in recnik:
                            neleksiprod.write(prefiks + ' (' + prefiks2 + ') : ' + rec + '\n')
                            zap = True
                            break
                    else:
                        pass
                if zap == False:
                    if rec[len(prefiks):] in recnik:
                        leksineprod.write(prefiks + ' : ' + rec + '\n')
                        zap = True
                    else:
                        neleksineprod.write(prefiks + ' : ' + rec + '\n')
                        zap = True

    with open('leksiprod.txt', 'w', encoding = 'utf-8') as leksiprod:
        with open('leksineprod.txt', 'w', encoding = 'utf-8') as leksineprod:
            with open('neleksineprod.txt', 'w', encoding = 'utf-8') as neleksineprod:
                with open('neleksiprod.txt', 'w', encoding = 'utf-8') as neleksiprod:
                    for rec in recnik:
                        prefiksator(rec)