num_subjects = int(input("Enter the number of subjects: "))

total_marks = 0

for i in range(num_subjects):
    marks = float(input(f"Enter the marks for subject {i+1}: "))
    total_marks += marks

average_marks = total_marks / num_subjects

print(f"The average marks are: {average_marks:.2f}")
