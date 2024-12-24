import random

def roll_dice():
    print("Welcome to the Dice Roller!");
    while True:
        try:
            # Get the number of sides on the dice
            sides = int(input("Enter the number of sides on the dice (e.g., 6 for a standard dice): "))
            if sides < 1: 
                print("Please enter a positive number of sides.")
                continue

            # Roll the dice
            result = random.randint(1, sides)
            print(f"You rolled a {result}!")

            # Ask if the user wants to roll again
            roll_again = input("Roll Again? (yes/no):").strip().lower()
            if roll_again not in ("yes", "y"):
                print("Thank you for using the dice roller! Goodbye!")
                break
            
        except ValueError:
            print("Invalid input, please enter a valid number. ")

if __name__ == "__main__":
    roll_dice()
