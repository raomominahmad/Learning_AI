# yield from and close the generator

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"


def imported_chai():
    yield "Matcha"
    yield "Oolong Tea"

def full_menu():
    yield from local_chai()
    yield from imported_chai()


# it means chai in local_chai and chai in imported chai iterate them separately one by one
for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, no more chai")


stall = chai_stall()
print(next(stall))
# cleaning up the memory to close the generator
stall.close


        