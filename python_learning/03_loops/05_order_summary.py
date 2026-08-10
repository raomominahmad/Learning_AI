# zip helps to iterate to multiple iterables
names = ["Momin" , "Ahmad" , "Ali" , "Hammad"]
bills = [50,70,100,55]

for name , amount in zip(names , bills):
    print(f"{name} paid {amount}")