# A file that opens one file, performs calculations and writes values #
# to a new file.                                                      #
# Calculations: square, cube, square root                             #
import math

read_file = input("Enter the file name with your integers: ")
write_file = input("Enter the output file name for: ")

infile = open(read_file, "r")
outfile = open(write_file, 'w')
outputString = ''
for line in infile:
    raw = int(line)
    square = int(line) ** 2
    cube = int(line) ** 3
    root = math.sqrt(int(line))
    outputString = str(raw) + " " + str(square) + " " + str(cube) + " " + str(root) + "\n"
    outfile.write(outputString)
    print(outputString)

infile.close()
outfile.close()
