def main():
    
    with open("string1.txt", "r") as f1:
        with open("string1_clean.txt", "w") as f2:  #felülírjuk (kicseréljük), ezért kell a "w"
            for i in f1:
                if '#' not in i:
                    f2.write(i)
    f1.close()
    f2.close()
    
    
if __name__=="__main__":
    main()