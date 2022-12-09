def main():
    x=79
    z=0
    y=-1
    print("A thought of a number between 1 and 100.")
    
    while x != y:
        y=int(input("your guess> "))
        if x>y:
            print("my number is larger")
        elif x<y:
            print("my number is smaller")
        z+=1
    
    print("Good job! That's it! \nNumber of guesses: {0}".format(z))    
        
        
if __name__=="__main__":
    main()