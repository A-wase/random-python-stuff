# Ask the user for their age. Stored as integer
age = int(input("Please enter your age: "))

# Check the age and print the corresponding message
if age >= 30:
    print("OH NO! You are a senior citizen.")
elif 18 <= age <= 29:
    print("Alright bro.")
elif 0 <= age <= 5:
    print("Bro was born too late, bro missed everything.")
elif age < 0:
    print("Hey! That's impossible.")
else:
    print("Enjoy your youth, kiddo!")