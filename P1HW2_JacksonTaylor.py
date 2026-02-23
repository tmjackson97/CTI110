# Taylor Jackson
# 2-23-2026
# P1HW2
# The program allows users to calculate their budget usage.

# Display program title
# Ask user to enter budget
# Ask user to enter travel destination
# Ask user to enter gas cost
# Ask user to enter accommodation cost
# Ask user to enter food cost
# Add gas, accommodation, and food expenses
# Subtract total expenses from budget
# Display formatted travel expense summary

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
print()

dest = (input("Enter your travel destination: "))
print()

gas = int(input("How much do you think you will spend on gas? "))
print()

acc = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()

food = int(input("Last, how much do you need for food? "))
print()

print("--------Travel Expenses--------")
print(f"Location: {dest}")
print(f"Intital Budget:{budget}")
print()

print(f"Fuel:{gas}")
print(f"Accommodation:{acc}")
print(f"Food:{food}")
print()

remain = budget - gas - acc - food 

print(f"Remaining Balance:{remain}")
