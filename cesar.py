def main():
    kod="kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    segit=[]
    megfejtes=[]
    
    for i in kod:
        segit.append(ord(i)-3)  #átalakítjuk unicode kódolás szerint
    for j in segit:
        megfejtes.append(chr(j))    #a kiszámolt számot visszaalakítjuk karakterré
    print("A visszakódolt szöveg: ","".join(megfejtes))
if __name__=="__main__":
    main()