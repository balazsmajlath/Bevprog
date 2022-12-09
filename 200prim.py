import prim as p

def main():
    x = 0
    for j in range(200):    
        if p.is_prime(j) == True:
            x += j

    print(x)
    
if __name__=="__main__":
    main()