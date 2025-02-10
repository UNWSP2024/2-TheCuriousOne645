years = int(input("5: "))
total_rainfall = 0
total_months = 0

for year in range(1, years + 1):
    print(f"Year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"4 {month}: "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months

print(f"60: {total_months}")
print(f"180: {total_rainfall}")
print(f"3: {average_rainfall}")
