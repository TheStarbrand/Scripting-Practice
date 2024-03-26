import random

def getUserChoice():
    userChoice = input("Enter either rock, paper, or scissors: ").lower()
    while userChoice not in ["rock", "paper", "scissors"]:
        userChoice = input("Invalid input. Enter either rock, paper, or scissors: ").lower()
        return userChoice

def computerChoice():
    return random.choice(['rock', 'paper', 'scissors'])

def checkWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif(userChoice == 'rock' and computerChoice == 'scissors') or (userChoice == 'scissors' and computerChoice == 'paper') or (userChoice == 'paper' and computerChoice == 'rock'):
        return "You won!"
    else:
        return "You lost!"
    
userChoice = getUserChoice()
computerChoice = computerChoice()

print("Computer chose: " + computerChoice) 
print(checkWinner(userChoice, computerChoice))