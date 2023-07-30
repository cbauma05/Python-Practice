import random

human_count = 0
computer_count = 0

print("----------------ROCK...PAPER...SCISSORS-----------------\n")
print("Let's Play!")

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").strip().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"The computer chooses: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        print("It's a Draw!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You Win!")
        global human_count #access global variable
        human_count += 1
    else:
        print("Computer Wins!")
        global computer_count #access global variable
        computer_count += 1

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    determine_winner(user_choice, computer_choice)

    answer = input("\nDo you want to play again? (yes/no): ").strip().lower()
    while answer not in ['yes', 'no']:
        answer = input("Invalid input. Please enter 'yes' or 'no': ").strip().lower()
    
    if answer == "no":
        break

print("\nThanks for playing the game!")
print(f"\nComputer score: {computer_count}")
print(f"Your score: {human_count}")

print("\nFinal Score:")
if computer_count > human_count:
    print("Computer Wins!")
elif computer_count == human_count:
    print("It's a Draw!")
else:
    print("Congratulations! You Win!")

