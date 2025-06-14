import random

def print_message():
    """
    This function prints a welcome message for the number guessing game.
    It informs the user about the rules and the range of numbers to guess from.
    """
    # Print a welcome message and prompt the user for input
    print("------------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("The computer has picked a number between 1 and 10.")
    print("Try to guess it! You'll be told if your guess is too low or too high.")
    print("------------------------------------------")


def get_user_input():
    """
    This function prompts the user for a guess and validates the input.
    It ensures that the input is a whole number between 1 and 100.
    """

    # Continuously prompt the user for input until a valid guess is provided
    while True:

        # Ask the user for a guess and validate the input
        user_input = input("Enter your guess (1-100): ")

        # Check if the input is valid using the validate_input function
        if validate_input(user_input):
            # If the input is valid, convert it to an integer and return it
            return int(user_input)
        
        else:
            # If the input is invalid, print an error message and prompt again
            print("Invalid input. Please enter a whole number between 1 and 100.")


def compare_guess(guess, target):
    """
    This function compares the user's guess with the target number and provides feedback.
    It informs the user if their guess is too low, too high, or correct.

    Args:
        guess (int): The user's guessed number.
        target (int): The target number that the user is trying to guess.
    """

    # Compare the user's guess with the target number and provide feedback
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")


def validate_input(input_value):
    """
    This function validates the user's input to ensure it is a whole number between 1 and 100.
    """
    # Validate if the input is a digit, return True if it is, otherwise return False
    return input_value.isdigit() and 1 <= int(input_value) <= 100


def main_game():
    """
    This function runs the main game loop for the number guessing game.
    """

    # Only have one target number for the whole game
    target = random.randint(1, 100)

    # Initialize the guess variable
    guess = None

    # If the guess is not equal to the target, keep asking for input
    while guess != target:
        guess = get_user_input()
        compare_guess(guess, target)


def run_game():
    """
    This function runs the number guessing game by printing a welcome message and starting the main game loop.
    """

    # Print the welcome message
    print_message()
    
    # Start the main game loop
    main_game()

# This is the entry point of the script
# It will run the game when the script is executed directly
if __name__ == "__main__":
    
    # Call the function to print a message based on user input
    run_game()