def main():
    total = 0
    year = 30
    apr = .06850
    # apr = .05850
    inv = 10000
    for i in range(30):
        fundsFromYear = ((1 + apr) ** year) * inv
        total = total + fundsFromYear
        print("Total amount that will be earned from funds deposited for", year, "years: $", round(fundsFromYear, 2))
        print("Total: $", round(total, 2))
        year -= 1

main()