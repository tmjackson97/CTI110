# Taylor Jackson
# 2-23-2026
# P1HW1 - Mathematical Expressions
# This program takes user input in the form of integers and performs math. 

print("-----Calculating Exponents-----")
print() 

base = int(input("Enter an integer as the base value:"))
exp = int (input("Enter an integer as the exponent:"))

power = base ** exp
print()
print(f"{base} raised to the power of {exp} is {power} !!")

print()
print("-----Addition and Subtraction-----")
print()

start = int(input("Enter a staring integer:"))
add_num = int(input("Enter an integer to add:"))
sub_num = int(input("Enter an integer to subtract:"))

result= start + add_num - sub_num

print()
print(f"{start} + {add_num} - {sub_num} is equal to {result}")
