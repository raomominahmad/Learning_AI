chai_type = "Ginger Chai"
customer_name = "Ali"

print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold more"
print(f"First word: {chai_description[:8]}")
print(f"First word: {chai_description[12:]}")
print(f"First word: {chai_description[::-1]}")

label_text = "Chai Spècial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded lable: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")

