def chai_customer():
    print("Welcome ! What chai whould you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        # again ask value using send it act as stoping condition for this loop
        order = yield

stall = chai_customer()
next(stall) # start thr generator


# send method interact with generator
stall.send("Masala Chai")
stall.send("Lemon Chai")