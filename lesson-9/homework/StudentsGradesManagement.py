import csv

grades = []

with open('grades.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Grade'] = int(row['Grade'])
        grades.append(row)

subject_grades = {}

for entry in grades:
    subject = entry['Subject']
    grade = entry['Grade']

    if subject not in subject_grades:
        subject_grades[subject] = []

    subject_grades[subject].append(grade)

average_grades = {subject: sum(grades)/len(grades) for subject, grades in subject_grades.items()}

with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)


    writer.writerow(['Subject', 'Average Grade'])

    for subject, average in average_grades.items():
        writer.writerow([subject, round(average, 2)])

print("average_grades.csv has been created successfully!")
