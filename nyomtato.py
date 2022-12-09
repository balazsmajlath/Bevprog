def main():
    
    oldal = "1-4,7,9,11-15"
    foldal = oldal.split(",")
    nyomold = [] #ebbe kerülnek majd a megoldás
    
    print(foldal)
    
    for i in foldal:
        if "-" in i: #megnézzük van-e benne -, mert akkor tól-ig
            ti = i.split("-")#két részre bontom
            for j in range(int(ti[0]), int(ti[1])+1): #sadly csak így engedi, mert túlmenne az indexen
                nyomold.append(j)#megadja a tólig az oldalakat
        else:#ha csak egy szám van
            nyomold.append(i)
    
    print(nyomold)
    
if __name__=="__main__":
    main()