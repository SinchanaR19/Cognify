import re

def check_password_strength(password):
    length_check = len(password) >= 8
    uppercase_check = bool(re.search(r'[A-Z]', password))
    lowercase_check = bool(re.search(r'[a-z]', password))
    digit_check = bool(re.search(r'[0-9]', password))
    special_char_check = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length_check, uppercase_check, lowercase_check, digit_check, special_char_check])

    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    print(f"\nPassword: {password}")
    print(f"Length >= 8: {'s' if length_check else 'n'}")
    print(f"Contains Uppercase: {'s' if uppercase_check else 'n'}")
    print(f"Contains Lowercase: {'s' if lowercase_check else 'n'}")
    print(f"Contains Digit: {'s' if digit_check else 'n'}")
    print(f"Contains Special Character: {'s' if special_char_check else 'n'}")
    print(f"\nPassword Strength: {strength}")

user_password = input("Enter your password: ")
check_password_strength(user_password)