chai = "Ginger chai"


def prepare_chai(order):
    print("Preparing", order)


prepare_chai(chai)
print(chai)

chai = [1, 2, 3]


def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Darjeeling", "Yes", "Low") #Postional
make_chai(tea="Green" ,sugar="Medium" , milk="No") #keyowrds

# *args — Collect positional arguments or * in a function signature — Keyword-only arguments
# **kwargs - collects keyword arguments into a dictionary

def special_chai(*ingredients , **extras):
    print("ingredients" , ingredients)
    print("Extras" , extras)

special_chai("Cinnamon" , "Cardmom" , sweetner="Honey" , foam = "yes")

# python uses same list instead of creating new one that is why default value should be 'None'
# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)


def chai_order(order=None):
    if order is None:
        order = []
    print(order)    

    
chai_order() 
chai_order()