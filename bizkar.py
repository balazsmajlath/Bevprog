def valid(text, chars):
    for i in text:
        for j in chars:
            if i == j:
                print(i)
text=input("Ide kérem a szöveget: ")
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
valid(text,chars)