favourite_chais = [
    "Masala Chai" , "Green Tea" , "Masala Chai" ,
    "Lemon Tea" , "Green Tea"  "Elaichi Chai"
]

# unique chai


# unique_chai = {chai for chai in favourite_chais if len(chai) >7 }
unique_chai = {chai for chai in favourite_chais}

# print(unique_chai)/

recipes = {
    "Masala Chai" : ["ginger" , "cardmom" ,  "clove"],
    "Elaichi" : ["cardmom" , "milk"],
     "Spicy Chai":["ginger" , "black pepper" , "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients }
# due to hashing in set output not remain same every time we run this file
print(unique_spices)