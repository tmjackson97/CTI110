# Taylor Jackson
# April 25, 2026
# P5LAB
# A self-checkout program that calculates change.

import random

def change(change):

    if change <= 0:
        if change == 0:
            print("No change owed.")
        else:
            print("Insufficient funds provided.")
        return

    total_cents = int(round(change * 100))

    num_dollars = total_cents // 100
    total_cents %= 100

    num_quarters = total_cents // 25
    total_cents %= 25

    num_dimes = total_cents // 10
    total_cents %= 10

    num_nickels = total_cents // 5
    total_cents %= 5

    num_pennies = total_cents

    if num_dollars > 0:
        print(f"{num_dollars} {'Dollar' if num_dollars == 1 else 'Dollars'}")
    if num_quarters > 0:
        print(f"{num_quarters} {'Quarter' if num_quarters == 1 else 'Quarters'}")
    if num_dimes > 0:
        print(f"{num_dimes} {'Dime' if num_dimes == 1 else 'Dimes'}")
    if num_nickels > 0:
        print(f"{num_nickels} {'Nickel' if num_nickels == 1 else 'Nickels'}")
    if num_pennies > 0:
        print(f"{num_pennies} {'Penny' if num_pennies == 1 else 'Pennies'}")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    cash_given = float(input("How much cash will you put in the self-checkout? "))

    change_owed = round(cash_given - amount_owed, 2)
    print(f"Change is: ${change_owed:.2f}")
    print()  
    change(change_owed)

if __name__ == "__main__":
    main()