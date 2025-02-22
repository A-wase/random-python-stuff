# Creating a function that checks is num is EVEN or ODD
def even_or_odd(num):
    return "EVEN" if num % 2 == 0 else "ODD"

num = int(input("Enter your number: "))
print(even_or_odd(num))  # Call the function and print result