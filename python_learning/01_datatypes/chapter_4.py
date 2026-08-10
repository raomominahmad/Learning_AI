is_boiling = True
stir_count = 5
# upcasting
total_actions = stir_count + is_boiling
print(f"Total actions: {total_actions}")

# no milk
milk_present = 0
print(f"Is there milk? {bool(milk_present)}")

# logical operation and or not
water_hot = True
tea_added = False

can_serve = water_hot or tea_added
print(f"Can serve chai? {can_serve}")
