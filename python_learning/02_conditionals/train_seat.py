# ticket info system
seat_type = input("Enter seat type: ").lower().strip()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air Conditioner system,comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")    
        