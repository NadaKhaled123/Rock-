import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid input! Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
user_wins = 0
for _ in range(6):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    print(winner)
    
    if winner == "You win!":
        user_wins += 1

# Check if the user has won at least once
if user_wins > 0:
    print("\nCongratulations! You won at least once.")
else:
    print("\nBetter luck next time!")
