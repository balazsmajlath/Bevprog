import prim as p

def main():
    
    for j in range(100):    
        if p.is_prime(j) == True:
            print(j, end = " ")

if __name__=="__main__":
    main()