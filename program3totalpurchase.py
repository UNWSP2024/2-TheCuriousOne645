# Program #3: Total Purchase
# Author: [Austin]
# Date: [1/29/2025]
# Title: Total Purchase Calculator

# Input prices of five items
item1 = float(input("Enter the price of item 1: $2.50"))
item2 = float(input("Enter the price of item 2: $4.70"))
item3 = float(input("Enter the price of item 3: $33.80"))
item4 = float(input("Enter the price of item 4: $55.80"))
item5 = float(input("Enter the price of item 5: $2.99"))

# Calculate subtotal
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate sales tax
sales_tax = subtotal * 0.07

# Calculate total
total = subtotal + sales_tax

# Display the results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
