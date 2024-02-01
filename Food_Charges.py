# Get the charge for the food from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip (18% of the food charge)

tip_percent = 0.18

tip_amount = food_charge * tip_percent

# Calculate the sales tax (7% of the food charge)

tax_percent = 0.07

tax_amount = food_charge * tax_percent

# Calculate the grand total

grand_total = food_charge + tip_amount + tax_amount

# Display the results

print(f"\nTip = ${tip_amount:.2f}")

print(f"Sales tax = ${tax_amount:.2f}")

print(f"Grand total = ${grand_total:.2f}")

