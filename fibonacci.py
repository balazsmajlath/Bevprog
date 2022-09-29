def main():

    n=int(input("n: "))
    x=0
    y=1
    k=0
    
    for _ in range(n-1):
        k=x+y
        x=y
        y=k

    print("Az {0}-dik elem értéke: {1}".format(n,k))
    
if __name__=="__main__":
    main()