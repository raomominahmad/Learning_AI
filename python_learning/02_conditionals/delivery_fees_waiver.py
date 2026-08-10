order_amount = int(input("Enter order amount for tea: "))

# ternary operator
delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_fees}")
