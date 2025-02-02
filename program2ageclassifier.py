# Get user's input for weight
weight = float(input("Enter the weight of the package in pounds: "))

# Determine the shipping cost based on weight
if weight <= 2:
    rate = 1.50
elif 2 < weight <= 6:
    rate = 3.00
elif 6 < weight <= 10:
    rate = 4.00
else:
    rate = 4.75

# Calculate the total cost
cost = weight * rate
print(f"The shipping cost is ${cost:.2f}")
