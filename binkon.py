def main(sz):
    if sz > 1:
        main(sz // 2)
    print(sz % 2, end = "")

sz = int(input("Kérek egy számot: "))
main(sz)
print()

if __name__ == "__main__":
    main()