# file = open("order.txt", "w")

# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")

# two dunder functions run when file operation are done file.__enter__() , file.__exit__()

