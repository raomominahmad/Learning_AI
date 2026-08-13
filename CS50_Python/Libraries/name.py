import sys
# sys.argv "argument vector"--> it is a list

if len(sys.argv) < 2:
    sys.exit("Two few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many argument")

for arg in sys.argv[1:]:
    print("hello, my name is",arg)

# print("hello , my name is", sys.argv[1])







# try:
#     print("hello, my name is",sys.argv[1]) # in sys.argv[0] name of file  in this case "name"
# except IndexError:
#     print("Too few Arguments")

