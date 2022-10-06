#működik csak a beszúrni kívánt szó mögött ne legyen pont vagy hasonló dolgok mert akkor azt az sz1-be is úgy kell írni
def main(litex, sz1, sz2):
    for i in litext:
        if i == sz1:
            print(sz2 + " " + i, end = " ")
        else:
            print(i, end=" ")
    print("")

text=input("Ide kérem az egész szöveget: ")
litext=list(text.split())
sz1=input("Az első szó: ")
sz2=input("A második szó: ")

main(litext,sz1, sz2)

if __name__=="__main__":
    main()