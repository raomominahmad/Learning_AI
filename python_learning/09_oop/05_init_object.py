class ChaiOrder:
    # type_ beacuse 'type' is a defined keyword
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("Masala" , 200)
print(order.summary())

order_two = ChaiOrder("Ginger" , 220)
print(order_two.summary())