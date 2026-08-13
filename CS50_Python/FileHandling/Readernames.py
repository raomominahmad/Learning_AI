names = []

with open("/home/momin/Documents/CS50P/Lecture6/data/names.txt","r") as file:
    for line in file:
       names.append(line.rstrip())

for name in sorted(names, reverse = True ): # reverse= True means sort in descending order
    print(f"hello, {name}")

# without using list and sorting the file variable
# with open("/home/momin/Documents/CS50P/Lecture6/data/names.txt","r") as file:
#     for line in sorted(file):
#        print("hello,", line.rstrip())


# with open("/home/momin/Documents/CS50P/Lecture6/data/names.txt","r") as file:
#     for line in file:
#         print("hello,", line.rstrip())









    # lines = file.readlines()  # readlines() reads and return data in form of list

# for line in lines:
#     print("hello,",line,end="")