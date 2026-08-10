menu = ["Green" , "Lemon" , "Spiced" , "Mint"]

for m in menu:
    print(f"Menu item is {m}")

# enumerate returns tuple
for idx, item in enumerate(menu):
    print(f"{idx} : {item} chai")
    