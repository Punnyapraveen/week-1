def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Check if the string is the same when reversed
    return s == s[::-1]

# Get input from the user
user_input = input("Enter a string: ")

# Call the function and print the result
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
