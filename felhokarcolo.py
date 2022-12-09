import math
def main():
    m = [2,4,8,3,9,7,1]
    magassag = 0 
    for i in range(1, len(m)):
        magassag = magassag + abs(m[i]-m[i-1])
        
    print("A magasságkülönbség: {0}".format(magassag))
    #második része
    x=2**1024
    li=[]
    magassag = 0

    for i in str(x):
        li.append(i)    #a szám szétszedése egy listába
    
    for i in range(1, len(li)):
        magassag += abs(int(li[i])-int(li[i-1]))
        
    print("A második feladat megoldása: {0}".format(magassag))
    
    
if __name__=="__main__":
    main()