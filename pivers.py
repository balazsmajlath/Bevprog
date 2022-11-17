def main():
    szov=[]
    with open("vers.txt", "r") as f:
        for i in f:
            szov.append(i)
    f.close() 
    with open("pi.txt", "w") as f2:       
        for j in szov:
            j=j.split(' ')
            print("Az elso szamjegy: ", len(j[0]), file=f2)
    f2.close()                   
            
if __name__=="__main__":
    main()    