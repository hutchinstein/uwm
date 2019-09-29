def main():
    binary = input("Enter your binary number: ")
    power = int(len(binary)) - 1
    base10 = 0
    for i in binary:
        a = int(i) * 2 ** power
        power -= 1
        base10 = base10 + a
    print(base10)

main()
