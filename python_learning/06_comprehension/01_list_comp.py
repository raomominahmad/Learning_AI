menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

# [expression for item in iterable  if condition]
iced_tea = [tea for tea in menu if "Iced" in tea]

print(iced_tea)