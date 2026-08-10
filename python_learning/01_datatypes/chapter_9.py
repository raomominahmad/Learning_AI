essential_spices = {"cardamom" , "ginger" , "cinnamon"}
optional_spices = {"cloves" , "ginger" , "black pepper"}

# union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")
# intersection
common_spices = essential_spices | optional_spices
print(f"common spices: {all_spices}")

# difference
only_in_essentials = essential_spices - optional_spices
print(f"Only in essential spices{only_in_essentials}")

print(f"is cloves is in optional spices? {'cloves' in optional_spices} ")

# freeze the list
mylist = ['apple' , 'banana' , 'cherry']
x = frozenset(mylist)

# it isimmutable
# x[1] = 'watermelon'