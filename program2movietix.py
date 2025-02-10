total_tickets = 0

while True:
    Sonic_3 = input("Enter the movie name (or type 'done' to finish): ")
    if Sonic_3.lower() == 'done':
        break
    num_tickets = int(input(f"How many tickets for {Sonic_3}? "))
    total_tickets += num_tickets

print(f"Total number of tickets desired: {total_tickets}")
