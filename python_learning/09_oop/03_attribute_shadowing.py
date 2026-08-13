# pyright: reportAttributeAccessIssue=false
class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ", cutting.temperature)
print("Direct look into the class " , Chai.temperature)
# this delete the instance's version not the class
del cutting.temperature
del cutting.cup
print(cutting.temperature)
# error for dynmaic attribute
print(cutting.cup)
