def is_palindrome(string):
    cleaned_string = string.lower().replace(" ", "")  # Convert string to lowercase and remove spaces
    return cleaned_string == cleaned_string[::-1]  # Compare with its reverse

string = str(input("Enter your string: "))
print(is_palindrome(string))
