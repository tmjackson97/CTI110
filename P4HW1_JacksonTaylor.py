# Taylor Jackson
# 04-10-2026
# P4HW1
# This program collects a user-defined number of scores, validates them using a loop, 
# drops the lowest score, and calculates the average and resulting letter grade.

def main():
    # Pseudocode:
    # 1. Ask the user how many scores they want to enter.
    # 2. Create an empty list.
    # 3. Loop to collect and validate scores (0-100).
    # 4. Drop the lowest score and calculate the average.
    # 5. Determine the letter grade and display results.

    num_scores = int(input("How many scores do you want to enter? "))
    score_list = []

    for i in range(num_scores):
        score = float(input(f"Enter score #{i + 1}: "))
        
        while score < 0 or score > 100:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            score = float(input(f"Enter score #{i + 1} again: "))
        
        score_list.append(score)

    lowest_score = min(score_list)
 
    modified_list = score_list.copy()
    modified_list.remove(lowest_score)

    average = sum(modified_list) / len(modified_list)

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print("\n--------------Results-----------")
    print(f"Lowest Score  : {lowest_score}")
    print(f"Modified List : {modified_list}")
    print(f"Scores Average: {average:.2f}")
    print(f"Grade         : {grade}")
    print("---------------------------------")

if __name__ == "__main__":
    main()