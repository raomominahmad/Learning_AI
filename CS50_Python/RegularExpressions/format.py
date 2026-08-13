import re
name = input("What's your name? ").strip()
# := walrus operator assign value after condition is true
if matches := re.search(r"^(.+), *(.+)$",name): # 0 or more spaces _ *
    name = matches.group(2) + " " + matches.group(1)

# if matches:
    # last , first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)

    # name = f"{first} {last}"

print(f"hello, {name}")


