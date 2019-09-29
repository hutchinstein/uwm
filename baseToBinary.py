def main():
    base10 = int(input("Enter your base 10 number: "))
    calculating = True
    binary = ""
    while calculating:
        a = base10%2
        # print("base 10 % 2 = ", base10, "%", "2 = ", a)
        z = base10//2
        # print("z = ", z)
        a = str(a)
        binary = a + binary
        base10 = z
        if z == 0:
            calculating = False

    print(binary)

main()
