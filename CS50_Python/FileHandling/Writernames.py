name = input("What's your name? ")

# through with keyword we can close file automatically
with open("/home/momin/Documents/CS50P/Lecture6/data/names.txt","a") as file:
    file.write(f"{name}\n")


# file = open("/home/momin/Documents/CS50P/Lecture6/data/names.txt","a")
#
# file.write(f"{name}\n")
# file.close()

# names = []
#
# for i in range(3):
#     names.append(input("What's your name? "))
#
# for name in sorted(names):
#     print(f"hello, {name}")