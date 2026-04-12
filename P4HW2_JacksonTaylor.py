# Taylor Jackson
# 04-10-2026
# P4HW2
# This program calculates payroll for multiple employees and tracks company totals.

def main():
    num_employees = 0
    total_overtime = 0
    total_regular = 0
    total_gross = 0

    name = input("Enter employee's name or \"Done\" to terminate: ")

    while name != "Done":
        hours = float(input(f"How many hours did {name} work? "))
        rate = float(input(f"What is {name}'s pay rate? "))
        num_employees += 1
        
        if hours > 40:
            overtime_hours = hours - 40
            reg_hours = 40
        else:
            overtime_hours = 0
            reg_hours = hours

        reg_pay = reg_hours * rate
        ot_pay = overtime_hours * (rate * 1.5)
        gross_pay = reg_pay + ot_pay

        total_regular += reg_pay
        total_overtime += ot_pay
        total_gross += gross_pay

        print("\nEmployee Name: ", name)
        print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'Overtime':<10}{'RegHour Pay':<15}{'OT Pay':<10}{'Gross Pay'}")
        print("-" * 80)
        print(f"{hours:<15.1f}{rate:<10.1f}{overtime_hours:<10.1f}{reg_pay:<15.2f}{ot_pay:<10.2f}{gross_pay:.2f}\n")

        name = input("Enter employee's name or \"Done\" to terminate: ")

    print(f"\nTotal number of employees entered: {num_employees}")
    print(f"Total amount paid for overtime: ${total_overtime:.2f}")
    print(f"Total amount paid for regular:  ${total_regular:.2f}")
    print(f"Total amount paid in gross:    ${total_gross:.2f}")
if __name__ == "__main__":
    main()