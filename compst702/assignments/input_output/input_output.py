import math

read_file = input("Enter the file name containing your values: ")
write_file = "PA5_output.txt"

infile = open(read_file, "r")
outfile = open(write_file, 'w')
outputString = ''

for line in infile:
    raw = int(line)
    square = int(line) ** 2
    cube = int(line) ** 3
    root = math.sqrt(int(line))

    print(raw, square, cube, root, file=outfile)
    print(raw, square, cube, root)
