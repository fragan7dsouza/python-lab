import csv
def input_student_data():
    student_data = []
    for i in range(5):
        usn = input("Enter USN for student {}:".format(i + 1))
        name = input("Enter Name for student {}:".format(i + 1))
        phone_number = input("Enter Phone Number for student {}:".format(i + 1))
        marks = float(input("Enter Marks for student {}:".format(i + 1)))
        student_data.append({'USN': usn, 'Name': name, 'Phone Number': phone_number, 'Marks': marks})
    return student_data

def write_to_csv(student_data, filename):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['USN', 'Name', 'Phone Number', 'Marks']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in student_data:
            writer.writerow(student)
filename = "student_info.csv"
student_data = input_student_data()
write_to_csv(student_data, filename)

top_scorer = max(student_data, key=lambda x: x['Marks'])
print("\nStudent Data (Sorted by USN):")
for student in student_data:
    print(student)
print("\nTop Scorer:")
print(top_scorer['Name'], "with USN", top_scorer['USN'], "scored", top_scorer['Marks'], "marks.")
