def form():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age. Please enter a positive number.")
    else:
        year = int(input("Enter the current year: "))

        if age >= 100:
            past_year = year - (age - 100)
            print(f"Hello {name}! You are already 100 or older!")
            print(f"You turned 100 in the year {past_year}.")
        else:
            x = 100 - age  # Calculate remaining years
            print(f"Hello {name}! You will turn 100 in {x} years.")
            print(f"You will turn 100 in the year {year + x}.")

# Start the loop
while True:
    form()
    other_person = input("Do you want to check on another person? (yes/no): ").strip().lower()
    
    if other_person == "no":
        print("Goodbye!")
        break  # Exit the loop if the user says no
