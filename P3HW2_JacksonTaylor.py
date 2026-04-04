# Taylor Jackson
# 3/27/2026
# P3HW2
# This program calculates an employee's weekly gross pay, including overtime for hours worked over 40, and displays a formatted summary of their earnings.

def main():
    name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        reg_hours = 40
    else:
        overtime_hours = 0
        overtime_pay = 0
        reg_hours = hours_worked

    reg_pay = reg_hours * pay_rate
    gross_pay = reg_pay + overtime_pay

    print("-" * 40)
    print(f"Employee name: {name}")
    print() 
    
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print("-" * 80)
    
    print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<15.2f}${reg_pay:<14.2f}${gross_pay:<.2f}")

if __name__ == "__main__":
    main()