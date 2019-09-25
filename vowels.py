vowels = ["a", "e", "i", "o", "u", "y"]


def main():
    vowelCount = 0
    word = input("Enter a word: ")
    word = word.lower()
    for i in word:
        if i in vowels:
            vowelCount += 1
            print("vowel!")
        print(i)
    print("The total number of vowels is:", vowelCount)


main()