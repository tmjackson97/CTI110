#Taylor Jackson
#2/28/2026
#P2LAB2
#

vehicles = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

keys = vehicles.keys()

print(keys)

vehicle_choice = input("Enter a vehicle to see it's mpg: ")

mpg = vehicles[vehicle_choice]
print(f"The {vehicle_choice} gets {mpg} mpg.")

miles = float(input(f"How many miles will you drive the {vehicle_choice}?"))

gallons_needed = miles / mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle_choice} {miles:.1f} miles.")