import random

user_win = 0
computer_win = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/paper/scissors or q to quit: ").lower()

    # Quit the game if the user inputs 'q'
    if user_input == 'q':
        break

    # Check if the input is valid
    elif user_input in options:
        # Generate computer's choice
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print("Computer picked %s" % computer_pick)

        # Handle equality case
        if user_input == computer_pick:
            print("Equality")
        # Handle user victory
        elif (user_input == "rock" and computer_pick == "scissors") or \
             (user_input == "scissors" and computer_pick == "paper") or \
             (user_input == "paper" and computer_pick == "rock"):
            print("You won!")
            user_win += 1
        # Handle computer victory
        else:
            print("Computer won!")
            computer_win += 1
    else:
        print("Invalid input. Please type rock/paper/scissors or q to quit.")
        continue

# Display results
print("You won %s times." % user_win)
print("Computer won %s times." % computer_win)
print("Goodbye!")

# Determine overall winner
if user_win > computer_win:
    print("Congratulations! You are the overall winner!")
elif user_win < computer_win:
    print("The computer wins overall! Better luck next time.")
else:
    print("It's a tie overall!")
