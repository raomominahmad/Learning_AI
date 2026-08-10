device_status = input("Enter status of device (offline/active) :").lower().strip()
temperature = int(input("Enter temperature for thermostats: "))

if device_status == "active":
    if temperature < 35:
        print("Normal")
    elif temperature > 35:
        print("High Temperature")

elif device_status == "offline":
    print("Device is offline")

else:
    print("Unknown status")