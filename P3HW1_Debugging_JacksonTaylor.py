# CTI-110
# P3HW1 - Grade List
# Taylor Jackson
# Dat3/26/26
# This program takes 6 module grades, calculates statistics, and displays a letter grade.

def main():
    # Enter grades for six modules
    mod_1 = float(input('Enter grade for Module 1: '))
    mod_2 = float(input('Enter grade for Module 2: '))
    mod_3 = float(input('Enter grade for Module 3: '))
    mod_4 = float(input('Enter grade for Module 4: '))
    mod_5 = float(input('Enter grade for Module 5: '))
    mod_6 = float(input('Enter grade for Module 6: '))

    # Add grades entered to a list
    grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

    # Calculate lowest, highest, sum, and average
    low = min(grades)
    high = max(grades)
    total_sum = sum(grades)
    avg = total_sum / len(grades)

    # Display results with formatted alignment
    print('\n------------Results------------')
    print(f'{"Lowest Grade:":<20}{low:.1f}')
    print(f'{"Highest Grade:":<20}{high:.1f}')
    print(f'{"Sum of Grades:":<20}{total_sum:.1f}')
    print(f'{"Average:":<20}{avg:.2f}')
    print('--------------------------------')

    # Determine letter grade for average
    if avg >= 90:
        print('Your grade is: A')
    elif avg >= 80:
        print('Your grade is: B')
    elif avg >= 70:
        print('Your grade is: C')
    elif avg >= 60:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

if __name__ == "__main__":
    main()