#2. Make a dictionary of student names and their scores.
# Write a function to find the student with the highest score.

students = {"Josh": 91, "Drake": 23, "Megan": 99, "Walter": 100}

def find_highest_score():
    highest_score = 0
    highest_student = ''

    for student, score in students.items():

        if score > highest_score:
            highest_score = score
            highest_student = student

    print(f"The highest score is {highest_student} with a score of {highest_score}")

find_highest_score()
