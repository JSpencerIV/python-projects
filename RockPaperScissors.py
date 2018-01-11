import random
# user greeting and instruction
print("Welcome to Rock,Scissors,paper")
# user input
userInput = raw_input("Pick Rock,Scissor,Paper: ")
print("you enter " + userInput)
# create array of objects for cpu to guess from
choices = ["rock","scissors","paper"]
# computer guest
computerGuess = random.choice(choices)
print(computerGuess)
# Resolve winner
if userInput == computerGuess:
    print("Draw")
elif userInput == "scissors" and computerGuess == "paper":
    print("User Wins")
elif userInput == "paper" and computerGuess == "rock":
    print("User Wins")
elif userInput == "rock" and computerGuess == "scissors":
    print("User Wins")
elif userInput == "rock" and computerGuess == "paper":
    print("Computer Wins")
elif userInput == "paper" and computerGuess == "scissor":
    print("Computer Wins")
elif userInput == "scissors" and computerGuess == "rock":
    print("Computer Wins")
# declare winner 

