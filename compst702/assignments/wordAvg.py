def main():
    sentence = input("Enter the sentence you would like analyzed: ")
    sentList = []
    sentList = sentence.split()
    counter = 0
    total = 0
    for i in sentList:
        total = total + len(i)
        counter += 1
    average = total/counter
    print("The average number of letters in each word in your sentence is:", average)
    print("The total number of words is: ", counter)
main()
