import random

def play_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        # Get user input
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Validate input
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Check guess
            if guess == target_number:
                print(f"\nCongratulations! You guessed the number {target_number} in {attempts} attempts!")
                return True
            elif guess < target_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

            # Show remaining attempts
            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # If max attempts reached
    print(f"\nGame Over! The number was {target_number}. Better luck next time!")
    return False

def main():
    while True:
        play_guessing_game()
        # Ask to replay
        replay = input("\nWould you like to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()