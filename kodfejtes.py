def main():
    
    uzenet = """
    Cbcq Dgyk!
    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!
    Aqmimjjyi:
    Ynyb"""
    megfejtes = """"""
    for i in range(0, len(uzenet)):
        #a megfejtés az adott karakter után lévő 2.karakter
        if ord(uzenet[i])+2 > 90 and ord(uzenet[i])<97: #különböző írásjelek vagy mik azok
            megfejtes = megfejtes + chr(ord(uzenet[i])-24)
        elif ord(uzenet[i])>63 and ord(uzenet[i])+2<=122: #nagy és kisbetűk
           megfejtes = megfejtes + chr(ord(uzenet[i])+2)
        elif ord(uzenet[i])+2>122: #zárójel meg ilyenek
            megfejtes = megfejtes + chr(ord(uzenet[i])-24)
        else: #maradék írásjel meg számok
            megfejtes = megfejtes+uzenet[i]
            
        
    print(megfejtes)
        
if __name__ == "__main__":
    main()