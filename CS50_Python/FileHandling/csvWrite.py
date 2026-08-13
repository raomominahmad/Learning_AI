import csv

name =input("What's your name? ")
home = input("Where's your home? ")
with open("/home/momin/Documents/CS50P/Lecture6/data/students2.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
