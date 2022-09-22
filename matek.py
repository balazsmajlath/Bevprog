import math


def main():
  
    a=int(input("a: "))
    b=int(input("b: "))
    c=int(input("c: "))
    
    p=math.sqrt(a*a+b*b)
    o1=(((-1*b) + math.sqrt(b*b-4*a*c))/2*a)
    o2=(((-1*b) - math.sqrt(b*b-4*a*c))/2*a)
    
    print('A megadott "a" sugárérték alapján a kör területe: {kt}'.format(kt=a*a*math.pi))
    print('A megadott "a" és "b" adatok alapján a pitagorasz-tétel eredménye: {0}'.format(p))
    print('A megadott számok alapján a másodfokú egyenlet megoldásai: {x1}; {x2}'.format(x1=o1,x2=o2))
if __name__=="__main__":
    main()