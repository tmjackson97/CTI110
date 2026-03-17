# Taylor Jackson
# 3-10-2026
# P2HW2
# This program collects grades for six modules, stores them in a list,
# and displays the lowest grade, highest grade, sum of grades, and average.

"""
Pseudocode:
1. Create an empty list to store grades
2. Ask the user to enter the grade for Module 1
3. Ask the user to enter the grade for Module 2
4. Ask the user to enter the grade for Module 3
5. Ask the user to enter the grade for Module 4
6. Ask the user to enter the grade for Module 5
7. Ask the user to enter the grade for Module 6
8. Store all grades in a list called module_grades
9. Find the lowest grade using min()
10. Find the highest grade using max()
11. Find the sum of grades using sum()
12. Calculate the average by dividing the sum by the number of grades
13. Display the results formatted like the example
"""
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for module 2: "))
module3 = float(input("Enter grade for module 3: "))
module4 = float(input("Enter grade for module 4: "))
module5 = float(input("Enter grade for module 5: "))
module6 = float(input("Enter grade for module 6: "))

module_grades = [module1, module2, module3, module4, module5, module6]

lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

print("/n----------Results----------")
print(f"Lowest Grade:     {lowest:.1f}")
print(f"Highest Grade:    {highest:.1f}")
print(f"Sum of Grades:    {total:.1f}")
print(f"Average:          {average:.2f}")
print("-----------------------------")