import re

email = input("What's your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): # ..*  can be used here which means at least one character, then zero or more characters.
#     print("Valid")

# if re.search(r"^\w+@\w+\.(edu|net|gov|com)$", email):
#     print("Valid") #edu|net|gov|com any domain and then "or" it
# /w --> A-Za-z0-9_
# ? 0 --> 0 or 1 repitition

if re.search(r"^(\w|.)+@(\w+\.)?\w+\.edu$", email , re.IGNORECASE):
    print("Valid") #(\w|.) --> . in username
else:
    print("Invalid")

# username, domain = email.split("@")
#
# if (username) and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")