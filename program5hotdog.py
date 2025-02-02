# Define prices
hotdog_price = 3.50
chili_dog_price = 4.50
cheese_price = 0.50
peppers_price = 0.75
onions_price = 1.00
tax_rate = 0.07

# Get user's input
hotdog_type = input("Enter the type of hot dog (Hot Dog/Chili Dog): ").lower()
toppings = input("Enter optional toppings (cheese, peppers, onions), separated by commas: ").lower().split(',')

# Calculate base cost
if hotdog_type == 'hot dog':
    base_cost = hotdog_price
elif hotdog_type == 'chili dog':
    base_cost = chili_dog_price
else:
    print("Invalid hot dog type")
    exit()

# Calculate toppings cost
toppings_cost = 0
if 'cheese' in toppings:
    toppings_cost += cheese_price
if 'peppers' in toppings:
    toppings_cost += peppers_price
if 'onions' in toppings:
    toppings_cost += onions_price

# Calculate total cost
subtotal = base_cost + toppings_cost
tax = subtotal * tax_rate
total_cost = subtotal + tax

# Display results
print(f"Hot Dog Cost: ${base_cost:.2f}")
print(f"Toppings Cost: ${toppings_cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
