total_tickets = 0

while True:
    movie_name = input("Enter the movie name (or type 'done' to finish): ")
    if movie_name.lower() == 'done':
        break
    num_tickets = int(input(f"How many tickets for {movie_name}? "))
    total_tickets += num_tickets

print(f"Total number of tickets desired: {total_tickets}")
