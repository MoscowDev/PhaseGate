from student_grade import *

print("Welcome to Lagbaja Schools Grade Management System!")

print("\nHow many students do you have?")
num_students = get_number_of_students()
print("\nSaving >>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Saved successfully")

print("\nHow many subjects do they offer?")
num_subjects = get_number_of_subjects()
print("\nSaving >>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("Saved successfully")

scores = get_scores(num_students, num_subjects)
print("\n Subject Scores data:")
for index, student_scores in enumerate(scores, start=1):
    print(f"Student {index}: {student_scores} score per subject")

print("\n=========================================")
print("Class Total score")
total_class = calculate_class_total(scores)
print(f"The total class score is: {total_class}")

print("\n=========================================")
print("Class Average score per student")
class_average = calculate_class_average(scores, num_subjects)
print(f"The class average (per subject across all students) is: {class_average:.2f}")

print("\n=========================================")
print("Total & Average score per student")
# Loop through each student to print their total and average
student_number = 1
students_averages = calculate_students_averages(scores)
for student_scores in scores:
    total = calculate_student_total(student_scores)
    average = calculate_student_average(total, num_subjects)
    print(f"Student {student_number}: Scores={student_scores}; Total={total}; Average={average:.2f}")
    student_number += 1

print("\n=========================================")
