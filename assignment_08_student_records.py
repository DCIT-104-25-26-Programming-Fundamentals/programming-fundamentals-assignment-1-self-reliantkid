# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


students = []

def add_student():
    student = {}
    try:
        name = input("Student name: ")
        id = input("Student ID: ")
        no_score = int(input("How many scores? "))

        if no_score <= 0:
            print("Enter at least one score\n")
            return

        scores = []

        for i in range(1, no_score+1):
            score = int(input(f"Enter score {i}: "))
            scores.append(score)

        student["name"] = name
        student["id"] = id
        student["scores"] = scores

        students.append(student)
        print(f'Student "{name}" added successfully.\n\n')
    except ValueError:
        print("Invalid value!\n")


def display_all():
    if len(students) == 0:
        print("No students have been added yet\n\n")
    else:
        print("--------------------------------------------------")
        print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average'}")
        print("--------------------------------------------------")

        for student in students:
            name = student["name"]
            id = student["id"]
            scores = ", ".join((str(sc) for sc in student["scores"]))

            _, avg = calc_average(id)

            print(f"{name:<15}{id:<12}{scores:<15}{avg}")

        print("\n")


def calc_average(student_id):
    try:

        student_details = next((student for student in students if student["id"] == student_id), None)

        if student_details == None:
            print("ID not found!")
            return None
        else:
            name = student_details["name"]
            scores = student_details["scores"]
            avg = round(sum(scores)/len(scores), 2)

            return name, avg
            
    except ValueError:
        print("Invalid value!\n")


def main():
    while True:
        print("================================")
        print("   STUDENT RECORD SYSTEM MENU   ")
        print("================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")

        try: 
            user_choice = int(input("\nEnter your choice (1-4): "))

            if user_choice not in range(1, 5):
                print("Option not in list!\n")
            else:
                if user_choice == 1:
                    add_student()
                elif user_choice == 2:
                    display_all()
                elif user_choice == 3:
                    s_id = input("Enter student ID: ")
                    result = calc_average(s_id)

                    if result is None:
                        print("ID not found\n")
                    else:
                        s_name, average = result
                        print(f"{s_name}'s average score: {average:.2f}\n")
                    
                elif user_choice == 4:
                    print("Goodbye!")
                    return
                
        except ValueError:
            print("Input must be a number in the options!\n")


main()