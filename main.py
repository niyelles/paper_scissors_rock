# Paper covers rock -> Paper wins
# Rock breaks scissors -> Rock wins
# Scissors cuts paper -> Scissors wins
# Make a variable called user input

# user input  == rock and computer input == scissors
# if user input is equal to rock and computer input is equal to scissors print user wins because {user input} beats {computer input}
#game_play = [rock, paper, scissors]
# write your code below this line ✌

user_input = input("Enter your choice (rock, paper, scissors): ")

import random

computer_input = random.choice(["rock", "paper", "scissors"])

if user_input == "rock" and computer_input == "scissors":
    print("User wins because rock beats scissors")
elif user_input == "paper" and computer_input == "rock":
    print("User wins because paper covers rock")
elif user_input == "scissors" and computer_input == "paper":
    print("User wins because scissors cut paper")
elif user_input == computer_input:
    print("It's a tie!")
else:
    print("Computer wins!")
