import csv

name =input("What's your name? ")
home = input("Where's your home? ")
with open("/home/momin/Documents/CS50P/Lecture6/data/students2.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})
