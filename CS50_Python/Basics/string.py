#  user about their name ( better approach)
name = input("What's your name?").strip().title()

# Split user's name into first name and last name
first , last = name.split(" ")

#remove whitespaces from str and capitalize user's name ( method-chaining )
# name = name.strip().title()

#  Capitalize user's name first letter
# name = name.capitalize()
# name = name.title()


# say hello to user
print(f"hello, {first}")