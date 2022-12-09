def main():
    x=input("Első szó: ")
    y=input("Második szó: ")
    
    if len(x) == len(y):
        xl = []
        yl = []

        for i in range(len(y)):
            if x[i] != " " or y[i] != "":
                xl.append(x[i].lower())
                yl.append(y[i].lower())
            
        if len(xl) != len(yl):
            print("Nem anagramma")
        else:
            xl.sort()
            yl.sort()
        
            if xl == yl:
                print("Anagramma")
            else:
                print("Nem anagramma")  
    else:
        print("Nem anagramma")
        
    
    
if __name__=="__main__":
    main()