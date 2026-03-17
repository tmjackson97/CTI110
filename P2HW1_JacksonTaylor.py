# Taylor Jackson
# 3-10-2026
# P2HW1
# This program calculates travel expenses and displays them in a formatted summary.

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
print()

dest = input("Enter your travel destination: ")
print()

gas = float(input("How much do you think you will spend on gas? "))
print()

acc = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))
print()

total = gas + acc + food
remain = budget - total

print("------------Travel Expenses------------")
print(f"{'Location:':<20}{dest}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${acc:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20}${remain:,.2f}")