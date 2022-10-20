class Garda:
    def __init__(self,nev,fiz,rang: str = "Junior",bede: int = 0):
        self.nev = nev
        self.rang = rang
        self.bede = bede
        self.fiz = fiz
            
    def emeles(self,osszeg: int = 10000):
        self.fiz += osszeg
    
    def evek(self):
        self.bede +=1
        
    def sorol(self):
        if self.bede < 1:
            self.rang = "Intern"
        elif self.bede < 2:
            self.rang = "Junior"
        elif self.bede < 5:
            self.rang = "Medior"
        else:
            self.rang = "Senior"
            
def main():
    a=Garda("Sanyi", 4000)
    
    a.emeles()
    a.emeles(465319)
    a.evek()
    a.sorol()
    
    print("Név: {0}\nFizetés: {1}\nRang: {2}\nBedolgozott évek: {3}".format(a.nev, a.fiz, a.rang, a.bede))

if __name__ == "__main__":
    main()