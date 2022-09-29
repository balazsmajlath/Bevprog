def main():
    
    sz=(input("Szám: "))
    csz=str(sz)
    rsz="".join(list(reversed(sz)))
    
    if sz==rsz:
        print("A {0} szám egy tükörszám.". format(sz))
    else:
        print("A {0} szám nem tükörszám.".format(sz))
    
if __name__=="__main__":
    main()