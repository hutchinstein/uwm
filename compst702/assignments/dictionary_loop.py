# A complete program for an "infinite" interactive loop to process a dictionary.


def main():
    d = {}  # dictionary

    # Read the file's contents in the dictionary d
    filename = input("Give the file name: ")
    file = open(filename, "r")
    for line in file:
        # read key and value
        key, value = line.split(",")
        # remove whitespaces before and after
        key = key.lstrip()
        key = key.rstrip()
        value = value.lstrip()
        value = value.rstrip()
        # insert entry in the dictionary
        d[key] = value

    file.close()

    loop = True  # continue looping if true
    saved = True

    while loop:
        print("\nEnter one of the following menu choices:")
        print("1 Add an entry")
        print("2 Show value for a key")
        print("3 Delete an entry")
        print("4 Save the file")
        print("5 Print the current dictionary")
        print("6 Quit")
        choice = input("Choice 1-6: ")
        print("\n")
        if choice == "1":  # Add an entry #
            k = input("Give the key: ")
            if k in d:
                r = input("This already exists, overwrite? (y/n) ")
                if r == "y":
                    v = input("Give its value: ")
                    d[k] = v
                else:
                    print("Key/value not changed")
            else:
                v = input("Give its value: ")
                d[k] = v
                saved = False
        elif choice == "2":  # Show value for a key #
            k = input("Give the key: ")
            l = list(d)
            if k in l:
                print(d[k])
            else:
                print("Key does not exist, please add to the dictionary")
        elif choice == "3":  # Delete an entry #
            k = input("Give the key to delete the entry: ")
            l = list(d)
            if k in l:
                del d[k]
                saved = False
            else:
                print(k + " does not exist, nothing to delete")
        elif choice == "4":  # Save the file #
            print("Saving the file")
            file = open(filename, "w")
            outstring = ""
            for i in d:
                outstring = outstring + i + ", " + d[i] + "\n"
            file.write(str(outstring))
            file.close()
            saved = True
        elif choice == "5":  # Print the current dictionary #
            l = list(d)
            l.sort()  # sort them
            sorted_dict = {}
            for i in l:
                sorted_dict[i] = d[i]
            print(sorted_dict)
        elif choice == "6":  # Quit #
            if not saved:
                r = input("List has changed, would you like to save first? (y/n) ")
                if r == "y":
                    continue
                else:
                    loop = False
                    continue
            else:
                loop = False
                continue
        else:
            print("Incorrect choice")


main()
