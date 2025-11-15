def get_number_of_students():
    num_students = -1
    while num_students <= 0:
        num_students = int(input("Enter the number of students: "))
        if num_students <= 0:
            print("Number of students must be greater than 0.")
    return num_students

def get_number_of_subjects():
    num_subjects = -1
    while num_subjects <= 0:
        num_subjects = int(input("Enter the number of subjects: "))
        if num_subjects <= 0:
            print("Number of subjects must be greater than 0.")
    return num_subjects

def get_scores(num_students, num_subjects):
    scores = []
    for student_index in range(num_students):
        student_scores = []
        print(f"\nEnter scores for Student {student_index + 1}:")
        for subject_index in range(num_subjects):
            score = -1
            while score < 0 or score > 100:
                score = int(input(f"  Enter score for subject {subject_index + 1}: "))
                if score < 0 or score > 100:
                    print("Invalid score! Must be between 0 and 100.")
            student_scores.append(score)
        scores.append(student_scores)
    return scores

def calculate_class_total(scores):
    total_class_score = 0
    for student_scores in scores:
        for score in student_scores:
            total_class_score += score
    return total_class_score

def calculate_class_average(scores, num_subjects):
    total_sum = 0
    num_students = len(scores)
    for student_scores in scores:
        for score in student_scores:
            total_sum += score
    total_count = num_students * num_subjects
    if total_count == 0:
        return 0
    class_average = total_sum / total_count
    return class_average

def calculate_student_total(student_scores):
    student_total = 0
    for score in student_scores:
        student_total += score
    return student_total

def calculate_students_averages(scores_per_student):
    averages = []
    for student_scores in scores_per_student:
        if len(student_scores) == 0:
            averages.append(0)
        else:
            total = sum(student_scores)
            average = total / len(student_scores)
            averages.append(average)
    return averages

def calculate_student_average(total_score, num_subjects):
    if num_subjects == 0:
        return 0
    return total_score / num_subjects
