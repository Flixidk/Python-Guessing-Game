import random

global high_score
high_score = 11

def main():
    global high_score
    print(
        "Welcome to the Number Guessing Game!\n" 
        "I'm thinking of a number between 1 and 100.\n"
        "You have 5 chances to guess the correct number.\n"
        )
    
    while True:
        print(
            "Please select the difficulty level:\n"
            "1. Easy (10 chances)\n"
            "2. Medium (5 chances)\n"
            "3. Hard (3 chances)\n"
            )
        
        while True:
            difficulty = input("Enter your choice: ")
            
            match difficulty:
                case "1":
                    total_guesses = 10
                    difficulty = "Easy"
                    break
                case "2":
                    total_guesses = 5
                    difficulty = "Medium"
                    break
                case "3":
                    total_guesses = 3
                    difficulty = "Hard"
                    break
                case _:
                    print("Please select a valid difficulty level!\n")

        print()
        print(
            f"Great! You have selected the {difficulty} difficulty level.\n"
            "Let's start the game!\n"
            )
        
        answer = random.randint(1, 100)
        guessed_correctly = False

        for i in range(total_guesses):
            guess = int(input("Enter your guess: "))

            if answer < guess:
                print(f"Incorrect! The number is less than {guess}")
            
            elif answer > guess:
                print(f"Incorrect! The number is greater than {guess}")
            
            else:
                print(f"\nCongratulations! You guessed the correct number in {i} attempts.")
                if i < high_score:
                    high_score = i
                guessed_correctly = True
                break
        
        if guessed_correctly == False:
            print("\nUnfortunately you have failed to guess the number!")

        while True:
            play_again = input("\nDo you want to play again? (Y/N): ")
            print()
            if play_again in ("Y", "N"):
                break
            print("Please enter a valid input (y/n).")

        if play_again == "N":
            print(f"High score = {high_score}")
            print("Thanks for playing! Goodbye 👋")
            break   
            
if __name__ == "__main__":
    main()