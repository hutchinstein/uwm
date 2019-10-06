binaryList = ["0001000001000000", "0001000101000001", "0111001000000001", "0001001101000010",
              "0001010001000011", "0111010100110100", "1000011000100101", "0011011011111111",
              "1100000000000000"]

hexdict = {
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


def load_func(register, operandA, operandB):
    print("LOAD register " + register + " with the bit pattern found in the memory cell whose address is "
          + operandA + operandB)


def loadbit_func(register, operandA, operandB):
    print("LOAD register " + register + " with the bit pattern "
          + operandA + operandB)


def store_func(register, operandA, operandB):
    print("STORE the bit pattern found in register " + register + " in the memory cell whose address is "
          + operandA + operandB)


def move_func(operandA, operandB):
    print("MOVE the bit pattern found in register " + operandA + " to register" + operandB)


def add_func(register, operandA, operandB):
    print("ADD the bit patterns in the registers " + operandA + " and " + operandB +
          " and leave the result in register " + register + " (the patterns in " + operandA +
          " and " + operandB + " are treated as 2s complement representation")


def addfloat_func(register, operandA, operandB):
    print("ADD the bit patterns in the registers " + operandA + " and " + operandB +
          " as though they represented values in floating-point notation and leave the floating-point "
          "result in register " + register)


def or_func(register, operandA, operandB):
    print("OR the bit patterns in registers " + operandA + " & " + operandB +
          " and place the result in register " + register)


def and_func(register, operandA, operandB):
    print("AND the bit patterns in registers " + operandA + " & " + operandB +
          " and place the result in register " + register)


def xor_func(register, operandA, operandB):
    print("")


# do not need operandA
def rotate_func(register, operandB):
    print("")


def jump_func(register, operandA, operandB):
    print("")


def main():
    for binaryString in binaryList:
        # Slice the binaryString to individual components
        opBin = binaryString[:4]
        register = binaryString[4:8]
        operandA = binaryString[8:12]
        operandB = binaryString[12:16]

        # Converts binary to hex
        opHex = hexdict[opBin]
        register = hexdict[register]
        operandA = hexdict[operandA]
        operandB = hexdict[operandB]

        print(opHex + register + operandA + operandB)
        if opHex == "1":
            load_func(register, operandA, operandB)
        elif opHex == "2":
            loadbit_func(register, operandA, operandB)
        elif opHex == "3":
            store_func(register, operandA, operandB)
        elif opHex == "4":
            move_func(operandA, operandB)
        elif opHex == "5":
            add_func(register, operandA, operandB)
        elif opHex == "6":
            addfloat_func(register, operandA, operandB)
        elif opHex == "7":
            or_func(register, operandA, operandB)
        elif opHex == "8":
            and_func(register, operandA, operandB)
        elif opHex == "9":
            xor_func(register, operandA, operandB)
        elif opHex == "A":
            rotate_func(register, operandB)
        elif opHex == "B":
            jump_func(register, operandB)
        elif opHex == "C":
            print("HALT the execution")

main()
