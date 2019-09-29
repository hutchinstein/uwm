##  futval.py
##  A program to compute the value of an investment
##  New Feature: User input to select duration of investment

def main():
    print("This program calculates the future value of an investment")
    print("You are able to select the initial investment, the interest rate and the duration")

    principal = int(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    duration = int(input("Enter the numbers of years of the investment: "))

    for i in range(duration):
        principal = principal * (1 + apr)

    principal = round(principal, 2)
    print("The value in year", duration, "is:", principal)


main()
