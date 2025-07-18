def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniformity
    cleaned = text.replace(" ", "").lower()
    
    # Check if cleaned string is the same when reversed
    return cleaned == cleaned[::-1]

# Get user input
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display result
if is_palindrome(user_input):
    print("It's a palindrome.")
else:
    print("Not a palindrome.")