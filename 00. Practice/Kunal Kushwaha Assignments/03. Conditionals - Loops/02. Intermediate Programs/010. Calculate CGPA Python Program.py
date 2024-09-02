num_subjects = int(input("Enter the number of subjects: "))

total_grade_points = 0

for i in range(num_subjects):
    grade_point = float(input(f"Enter the grade point for subject {i+1}: "))
    total_grade_points += grade_point

cgpa = total_grade_points / num_subjects

print(f"The CGPA is: {cgpa:.2f}")
