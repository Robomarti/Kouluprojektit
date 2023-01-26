import string

def printtaa(printattava: str):
    try:
        printtausLista.append(muuttujat[printattava])
    except KeyError:
        printtausLista.append(int(printattava))

def aseta_arvo(muuttujanNimi: str, muuttujanArvo: str):
    try:
        muuttujat[muuttujanNimi] = int(muuttujanArvo)
    except:
        muuttujat[muuttujanNimi] = int(muuttujat[muuttujanArvo])

def lisaa_arvo(muuttujanNimi: str, muuttujanArvo: str):
    try:
        muuttujat[muuttujanNimi] += int(muuttujanArvo)
    except:
        muuttujat[muuttujanNimi] += int(muuttujat[muuttujanArvo])

def vahenna_arvo(muuttujanNimi: str, muuttujanArvo: str):
    try:
        muuttujat[muuttujanNimi] -= int(muuttujanArvo)
    except:
        muuttujat[muuttujanNimi] -= int(muuttujat[muuttujanArvo])

def kerro_arvo(muuttujanNimi: str, muuttujanArvo: str):
    try:
        muuttujat[muuttujanNimi] *= int(muuttujanArvo)
    except:
        muuttujat[muuttujanNimi] *= int(muuttujat[muuttujanArvo])

def aseta_kohta(kohdanNimi: str, kohtaListassa: int):
    hyppykohdat[kohdanNimi] = str(kohtaListassa)

def hyppaa_kohtaan(hyppykohta: str):
    try:
        return int(hyppykohdat[hyppykohta])
    except:
        print("voi vittu")
        return "moi"

def onko_Totta(arvo1: str, ehto: str, arvo2: str):
    mArvo1 = 0
    mArvo2 = 0
    try:
        mArvo1 = int(arvo1)
    except:
        mArvo1 = int(muuttujat[arvo1])
    try:
        mArvo2 = int(arvo2)
    except:
        mArvo2 = int(muuttujat[arvo2])
    if ehto == "==":
        return mArvo1 == mArvo2
    elif ehto == "!=":
        return not mArvo1 == mArvo2
    elif ehto == "<":
        return mArvo1 < mArvo2
    elif ehto == ">":
        return mArvo1 > mArvo2
    elif ehto == "<=":
        return mArvo1 <= mArvo2
    elif ehto == ">=":
        return mArvo1 >= mArvo2

def suorita(ohjelma: list):
    global muuttujat #luodaan globaali sanakirja
    if "muuttujat" not in globals():
        muuttujat = {}
    global hyppykohdat #luodaan globaali sanakirja
    if "hyppykohdat" not in globals():
        hyppykohdat = {}
    
    global printtausLista #luodaan globaali lista
    if "printtausLista" not in globals():
        printtausLista = []
    
    for kirjain in string.ascii_uppercase:
        muuttujat[kirjain] = 0
    
    for z in range(len(ohjelma)): #alustetaan kaikki hyppy kohdat
        kaskyt = str(ohjelma[z]).split(" ")
        if len(kaskyt) == 1:
            kaskyt[0] = kaskyt[0].replace(":", "")
            aseta_kohta(kaskyt[0], z)

    i = 0
    while i < len(ohjelma):
        kaskyt = str(ohjelma[i]).split(" ")
        if kaskyt[0] == "PRINT":
            printtaa(kaskyt[1])
        elif kaskyt[0] == "MOV":
            aseta_arvo(kaskyt[1], kaskyt[2])
        elif kaskyt[0] == "ADD":
            lisaa_arvo(kaskyt[1], kaskyt[2])
        elif kaskyt[0] == "SUB":
            vahenna_arvo(kaskyt[1], kaskyt[2])
        elif kaskyt[0] == "MUL":
            kerro_arvo(kaskyt[1], kaskyt[2])
        elif kaskyt[0] == "JUMP":
            kaskyt[1] = kaskyt[1].replace(":", "")
            try:
                i = int(hyppaa_kohtaan(kaskyt[1]))
            except ValueError:
                i = i
        elif kaskyt[0] == "IF":
            if onko_Totta(kaskyt[1], kaskyt[2], kaskyt[3]):
                kaskyt[5] = kaskyt[5].replace(":", "")
                try:
                    i = int(hyppaa_kohtaan(kaskyt[5]))
                except ValueError:
                    i = i
        elif kaskyt[0] == "END":
            break
        else:
            pass
        i += 1
    
    muuttujat.clear()
    hyppykohdat.clear()
    palautusLista = printtausLista.copy()
    printtausLista.clear()
    return palautusLista

def koodi():
  #tässä voi testata koodia
  suorituskoodi = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'alku:', 'MOV B 2', 'MOV Z 0', 'testi:', 'MOV C B', 'uusi:', 'IF C == A JUMP virhe', 'IF C > A JUMP ohi', 'ADD C B', 'JUMP uusi', 'virhe:', 'MOV Z 1', 'JUMP ohi2', 'ohi:', 'ADD B 1', 'IF B < A JUMP testi', 'ohi2:', 'IF Z == 1 JUMP ohi3', 'PRINT A', 'ohi3:', 'ADD A 1', 'IF A <= N JUMP alku']
  print(suorita(suorituskoodi))
