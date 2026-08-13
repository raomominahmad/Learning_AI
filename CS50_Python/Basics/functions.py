def main ():
    name = input("What's your name? ")
    hello(name)


def hello(to = "world") :
    print("hello,",to)

#  call to main function
main()




# default value of to will be "world"
# def hello ( to="world" ):
#     print("hello,", to)
# hello()
# name = input("What's your name? ")
# hello(name)
#
# # print(name)