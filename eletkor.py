def main():
    
    a=int(input("age: "))
    
    if a>=21:
        print("Fogyaszthat alkoholt Amerikában.")
    else:
        print("Nem fogyaszthat alkoholt Amerikában.")
    
    if a>=18:
        print("Magyarországon vásárolhat dohányterméket.")
    else:
        print("Magyarországon nem vásárolhat dohányterméket.")
    
    if a>=16:
        print("Szerezhet jogosítványt.")
    else:
        print("Nem szerezhet jogosítványt.")
    
    if a>=12:
        print("Megnézheti egyedül a Shrek 2-t.")
    else:
        print("Nem nézheti meg egyedül a Shrek 2-t.")
            
if __name__=="__main__":
    main()