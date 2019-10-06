lib = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
    }

hexString = ""
binary = str(input("Enter the binary string to convert to hex: "))
print(len(binary))
while len(binary) >= 4:
    a = binary[:4]
    z = lib.get(a)
    hexString = hexString + z
    print("hexString: ", hexString)
    #print(a)
    binary = binary[4:]
    #print(binary)
