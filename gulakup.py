import math

def main():
    
    a=int(input("A kör sugara: "))
    b=int(input("A téglalap egyik oldala: "))
    c=int(input("A téglalap másik oldala: "))
    d=int(input("A test magassága: "))
    kt=math.pi*a*a
    tt=b*c
    kut=(1/3)*kt*d
    
    print("A kör területe: {k} \nA téglalap területe: {t}\nA kúp térfogata, a kör területéből: {té}".format(k=kt,t=tt,té=kut))
    
if __name__=="__main__":
    main()