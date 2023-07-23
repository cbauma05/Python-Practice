import random

human_count = 0
computer_count = 0

continue_game = True

print("----------------ROCK...PAPER...SCISSORS--------------\n")
print("Let's Play!")

while continue_game:

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print('The computer chooses' + computer_choice)

    human_choice = random.choice(['rock', 'paper', 'scissors'])
    print('Human chooses' + human_choice)

    if((human_choice == 'rock' and computer_choice == 'scissors' and computer_choice == 'paper') or (human_choice == 'paper' and computer_choice == 'rock')):
        print("Human Wins!")
        human_count += 1
    elif(human_choice == computer_choice):
        print("Draw")
    else:
        print("Computer Wins!")
        computer_count += 1

    print("\nWould you like to play again?")
    answer = input()
    if answer == "no":
        print("\nThanks for playing the game!")
        print("\nComputer score is: " + str(computer_count))
        print("\nHuman score is " + str(human_count))

        print("\nFinal Score:")
        if computer_count > human_count:
            print("Computer Wins!!")
        elif computer_count == human_count:
            print("\nIt is a Draw")
        else:
            print("You Win\n")
