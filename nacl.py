def main():
    
    na=int(input("Na db: "))
    cl=int(input("Cl db: "))
    nacl=0
    mna=0
    mcl=0
    
    if na==cl:
        nacl=na     
    elif na>cl:
        nacl=cl
        mna=na-cl
    elif na<cl:
        nacl=na
        mcl=cl-na
    if nacl%2==0:
        print("A megadott mennyiségek alapján {0} db NaCl keletkezett, {1} db Na és {2} db Cl maradt".format(nacl,mna,mcl))
    else:
        nacl=nacl-1
        mna=mna+1
        mcl=mcl+1 
        print("A megadott mennyiségek alapján {0} db NaCl keletkezett, {1} db Na és {2} db Cl maradt".format(nacl, mna, mcl))
        
if __name__=="__main__":
    main()