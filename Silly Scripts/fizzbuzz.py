for num in range(1, 101):  # Looping through numbers 1 to 100
    if num % 3 == 0 and num % 5 == 0:  # Check if the number is a multiple of both 3 and 5
        print("fizzbuzz")
    elif num % 3 == 0:  # Check if the number is a multiple of 3
        print("fizz")
    elif num % 5 == 0:  # Check if the number is a multiple of 5
        print("buzz")
    else:
        print(num)  # Print the number if it is neither a multiple of 3 nor 5