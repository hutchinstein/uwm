def wordsInFile(filename):
    myFile = open(filename, "r")
    wordCounter = 0
    for line in myFile:
        wordList = line.split(" ")
        wordCounter += len(wordList)
    return wordCounter


def linesInFile(filename):
    lineCounter = 0
    myFile = open(filename, "r")
    for line in myFile:
        lineCounter += 1
    return lineCounter


def main():
    file1 = input("Give a file name: ")
    print("Number of lines in file", file1, "are:", linesInFile(file1))
    print("Number of words in file", file1, "are:", wordsInFile(file1))
    file2 = input("\nGive another file name: ")
    print("Number of lines in file", file2, "are:", linesInFile(file2))
    print("Number of words in file", file2, "are:", wordsInFile(file2))

main()
