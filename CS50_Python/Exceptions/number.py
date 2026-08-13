def main():
    x = get_int("Whats's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
         # x = int(input("What's x? "))
         # break
         # return x
        except ValueError:
            # do nothing on catching error
            pass
         # print("x is not an integer")
        # else:
        #     # break
        #     return x


main()

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")



