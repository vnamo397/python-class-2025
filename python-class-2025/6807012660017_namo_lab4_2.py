# Student Score Recorder for 50 students
import random

def get_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

students = {}
subjects = ['Eng', 'Com', 'Net', 'Math']


for i in range(1, 51):
    student_id = f"S{i:03d}"
    scores = {subj: random.randint(0, 100) for subj in subjects}
    grades = {subj: get_grade(scores[subj]) for subj in subjects}
    total = sum(scores.values())
    avg = total / 4
    # Calculate GPA-like value (A=4, B=3, C=2, D=1, F=0)
    grade_point = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    gpa = sum(grade_point[grades[subj]] for subj in subjects) / 4
    # Ensure GPA does not exceed 4.00
    grades['Sum'] = round(min(gpa, 4.00),2 )
    students[student_id] = grades

# Print all students' results
for sid, info in students.items():
    print(f"{sid}: {info}")