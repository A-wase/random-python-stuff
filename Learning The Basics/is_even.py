# Create a Python function called is_even that takes a single integer
# as input and returns True if the number is even, and False if it is odd.

def is_even(number):
    return number % 2 == 0

# Example usage:
if __name__ == "__main__":
    print(is_even(4))  # Output: True
    print(is_even(5))  # Output: False
    print(is_even(0))  # Output: True
    print(is_even(-2)) # Output: True
    print(is_even(-3)) # Output: False