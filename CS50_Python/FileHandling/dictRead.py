import csv

students = []

with open("/home/momin/Documents/CS50P/Lecture6/data/students2.csv","r") as file:
   reader = csv.DictReader(file)
   for row in reader:
       # students.append({"name":row["name"],"home":row["home"]})
       # or
       students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
       print(f"{student['name']} is from {student['home']}")