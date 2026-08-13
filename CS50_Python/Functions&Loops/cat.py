def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for I in  range(n):
        print("meow")

main()

while True :
    n = int(input("What's n? "))
    if n > 0:
        break

for i in range(n):
    print("meow")



 by default range start from zero in this case 0, 1, 2 less than number inside in range
for i in range(3):
    print("meow")

'_" underscore is placeholder for variable that is not used inside a loop
for _ in range(3):
    print("meow")

    another approach
print("meow\n"*3,end="")


for i in [0 , 1 ,2] :
    print("meow")




i = 0
while i < 3:
    print("meow")
    i += 1
