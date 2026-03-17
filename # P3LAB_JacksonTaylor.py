# P3LAB_JacksonTaylor
# Date: March 17, 2026
# Description: This program calculates the most efficient number of dollars, 
# quarters, dimes, nickels, and pennies for a given float amount.

def main():
    user_input = input("Enter the amount of money as a float: ")
    try:
        amount = float(user_input.replace('$', ''))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return
    
    if amount == 0:
        print("No change")
        return
    
    total_cents = int(round(amount * 100))

    dollars = total_cents // 100
    total_cents %= 100

    quarters = total_cents // 25
    total_cents %= 25

    dimes = total_cents // 10
    total_cents %= 10

    nickels = total_cents // 5 
    total_cents %= 5

    pennies = total_cents

    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")
            
    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")

if __name__ == "__main__":
    main()