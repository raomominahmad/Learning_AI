def main():
    # print_row(4)
    # print_column(3)
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        # print space for each iteration
        print()

def print_row( width ):
    print("?"*width)


def print_column(height):
        print("#\n"*height , end="")

main()