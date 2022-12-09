class Verem:
    def __init__(self, t=[]) -> None:
        self.t = t  #a verem tartalma

    def ures(self):
        if self.t==[]:
            return True
        else:
            return False
        
    def betesz(self, szam):
        self.t.append(szam)
        
    def kivesz(self):
        return self.t.reverse.pop()
        
    def meret(self):
        return len(self.t)    
        
def main():
    
    v = Verem()
    print(v.t)   
    v.ures()
    x = int(input("Ezt a számot tegyük bele> "))
    v.betesz(x)
    print(v.t)         
    print(v.meret()) 
    print(v.ures())  
    x = v.kivesz()
    print(x)         
    print(v.t)         
    v.kivesz()
    v.kivesz()       
    x = v.kivesz()
    print(x)
    
if __name__=="__main__":
    main()