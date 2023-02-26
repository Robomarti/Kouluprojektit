class Nelilaskin:
    def Plussaa(self):
        print("Yhteenlasku (+)")
        luku1 = float(input("Anna 1. luku: "))
        luku2 = float(input("Anna 2. luku: "))
        tulos = luku1 + luku2
        print(f"Tulos: {tulos}")
        self.LisaaHistoriaan(self, f"{luku1};+;{luku2};{tulos}")

    def Vahenna(self):
        print("Vähennyslasku (-)")
        luku1 = float(input("Anna 1. luku: "))
        luku2 = float(input("Anna 2. luku: "))
        tulos = luku1 - luku2
        print(f"Tulos: {tulos}")
        self.LisaaHistoriaan(self, f"{luku1};-;{luku2};{tulos}")
    
    def Kerro(self):
        print("Kertolasku (*)")
        luku1 = float(input("Anna 1. luku: "))
        luku2 = float(input("Anna 2. luku: "))
        tulos = luku1 * luku2
        print(f"Tulos: {tulos}")
        self.LisaaHistoriaan(self, f"{luku1};*;{luku2};{tulos}")
    
    def Jaa(self):
        print("Jakolasku (/)")
        luku1 = float(input("Anna 1. luku: "))
        luku2 = float(input("Anna 2. luku: "))
        tulos = luku1 / luku2
        print(f"Tulos: {tulos}")
        self.LisaaHistoriaan(self, f"{luku1};/;{luku2};{tulos}")

    def HistoriaCount(self):
        with open("historia.txt", "r") as tiedosto:
            return len(tiedosto.readlines())
    
    def Historia(self):
        pituus = self.HistoriaCount(self)
        if pituus < 1:
            print("Historiatietoja ei saatavilla.")
        elif pituus >= 1:
            if pituus == 1:
                print(f"Historiassa 1 tulos:")
            else:
                print(f"Historiassa {pituus} tulosta:")

            with open("historia.txt", "r") as tiedosto:
                for rivi in tiedosto:
                    osat = rivi.split(";")
                    print(f"{osat[0]} {osat[1]} {osat[2]} = {osat[3]}", end="") 
                tiedosto.close()                                                
    
    def TyhjennaHistoria(self):
        with open("historia.txt", "w") as tiedosto:
            tiedosto.close()
        print("Historia tyhjennetty.")
    
    def LisaaHistoriaan(self, lisays):
        with open("historia.txt", "a") as tiedosto:
            tiedosto.write(lisays + "\n")
            tiedosto.close()

    def Tiedot(self):
        print("Toiminnot:\n0 - ohjelman lopettaminen\n1 - laske yhteenlasku (+)\n2 - laske vähennyslasku (-)")
        print("3 - laske kertolasku (*)\n4 - laske jakolasku (/)\n5 - näytä historia\n6 - tyhjennä historia\n7 - näytä toiminnot")

    def Suorita(self):
        with open("historia.txt", "a") as tiedosto: #jos tiedostoa ei ole, se luodaan tässä
            tiedosto.close()
        if self.HistoriaCount(self) == 1:
            print(f"Nelilaskin\nHistoriassa {self.HistoriaCount(self)} tulos")
        else:
            print(f"Nelilaskin\nHistoriassa {self.HistoriaCount(self)} tulosta")
        self.Tiedot(self)
        while True:
            luku = float(input("Valitse toiminto: "))
            if luku == 0:
                print("Lopetetaan...")
                break
            elif luku == 1:
                self.Plussaa(self)
            elif luku == 2:
                self.Vahenna(self)
            elif luku == 3:
                self.Kerro(self)
            elif luku == 4:
                self.Jaa(self)
            elif luku == 5:
                self.Historia(self)
            elif luku == 6:
                self.TyhjennaHistoria(self)
            elif luku == 7:
                self.Tiedot(self)
  
laskin = Nelilaskin
laskin.Suorita(laskin)
