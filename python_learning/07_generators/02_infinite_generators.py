def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

# Control how many values to take from the infinite generator
for _ in range(5):
    print(next(refill))

# values are not inter mixing
for _ in range(6):
    print(next(user2))


