def determine_grade(marks):
    if 91 <= marks <= 100:
        return "AA"
    elif 81 <= marks <= 90:
        return "AB"
    elif 71 <= marks <= 80:
        return "BB"
    elif 61 <= marks <= 70:
        return "BC"
    elif 51 <= marks <= 60:
        return "CD"
    elif 41 <= marks <= 50:
        return "DD"
    elif marks <= 40:
        return "Fail"
    else:
        return "Invalid marks"


input_marks = int(input("Enter your marks out of 100: "))

grade = determine_grade(input_marks)

print(f"Your grade is: {grade}")
