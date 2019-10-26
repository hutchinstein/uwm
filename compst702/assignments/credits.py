def creditCalculation(n):
    if n < 7:
        return "Freshman"
    if 7 <= n < 16:
        return "Sophomore"
    if 16 <= n < 26:
        return "Junior"
    elif n >= 26:
        return "Senior"


def main():
    creditsEarned = input("Enter the number of credits the student has earned: ")
    print(creditCalculation(int(creditsEarned)))

main()