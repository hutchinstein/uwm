def main():
    base10 = int(input("Enter your base 10 number: "))
    calculating = True
    binary = ""
    while calculating:
        a = base10 % 2
        # print("base 10 % 2 = ", base10, "%", "2 = ", a)
        z = base10//2
        # print("z = ", z)
        a = str(a)
        # print(str(base10) + "/2,", z, ",", a)
        binary = a + binary
        base10 = z
        if z == 0:
            calculating = False
    print(binary)
while True:
    main()
