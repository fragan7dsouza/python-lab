def calculate_average(grades):
    return sum(grades) / len(grades)

def calculate_student_grades(student):
    name = student['name']
    grades = [student['math'], student['english'], student['science']]
    average_grade = calculate_average(grades)
    return f"{name}: {average_grade:.2f}"
def calculate_class_average(students):
    total_grades = 0
    num_grades = 0
    for student in students:
        for key, value in student.items():
            if key != 'name':
                total_grades += value
                num_grades += 1
    return total_grades / num_grades
students = []
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    math_grade = float(input("Enter the math grade: "))
    english_grade = float(input("Enter the english grade: "))
    science_grade = float(input("Enter the science grade: "))
    student = {'name': name, 'math': math_grade, 'english': english_grade, 'science': science_grade}
    students.append(student)

print("Grades for each student:")
for student in students:
    print(calculate_student_grades(student))

class_average = calculate_class_average(students)
print(f"\nClass average: {class_average:.2f}")

