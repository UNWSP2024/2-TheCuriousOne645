def kilometers_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

def main():
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers_to_miles(kilometers)
    print(f"{kilometers} kilometers is equal to {miles} miles.")

if __name__ == "__main__":
    main()
