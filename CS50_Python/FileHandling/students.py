students = []
# with open("/home/momin/Documents/CS50P/Lecture6/data/students.csv","r") as file:
#     for line in file:
#         name , house  = line.rstrip().split(",")
#         print(f"{name} is in {house}")

#  another approach of creating dicitonary

with open("/home/momin/Documents/CS50P/Lecture6/data/students2.csv","r") as file:
   for line in file:
       name,home = line.rstrip().split(",")
       student = {"name": name , "home": home}
       # student ={}
       # student["name"] = name
       # student["house"] = house
       students.append(student)

# def get_name(student):
#   return student["name"]

# def get_house(student):
#      return student["house"]

# for student in sorted(students , key = get_house, reverse = True ):
#     print(f"{student['name']} is in {student['house']}")

# lamba which is an anonymus function can used

for student in sorted(students , key = lambda student: student["name"] ):
    print(f"{student['name']} is from {student['home']}")


#     for line in file:
#         name,house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)
