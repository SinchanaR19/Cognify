import random

def number_guessing_game():
    print("🎯 Welcome to the Range-Based Number Guessing Game!")

    # Get range from user
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start >= end:
            print("Invalid range. Start must be less than end.")
            return

        # Generate random number in range
        number_to_guess = random.randint(start, end)
        attempts = 0

        print(f"I have picked a number between {start} and {end}. Try to guess it!")

        # Start guessing loop
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < start or guess > end:
                    print(f"Please guess a number between {start} and {end}.")
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f" Correct! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    except ValueError:
        print("Invalid input. Please enter valid integers for the range.")
number_guessing_game()