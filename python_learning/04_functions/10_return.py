def make_chai():
    # return "Here is your masala chai"
    print()

return_value = make_chai()
print(return_value)    

# None
def idle_chaiwala():
    pass

print(idle_chaiwala())

# one value
def solid_cups():
    return 120

total = solid_cups()
print(total)


def chai_status(cups_left):
    if cups_left == 0:
        return 'Sorry, chai over'
    return "Chai is ready"    

chai_status(5)
print(chai_status(0))
print(chai_status(5))

# Multiple values
def chai_report():
    return 100,20,10  #sold, remaining

sold , remaining  , not_paid = chai_report()

print("Sold:",sold)
print("Remaining:",remaining)
        
        


