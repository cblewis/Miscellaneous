import random

#Masterfully Crafted by Cameron Lewis

playerChoice = input("Please type rock, paper, or scissors to play: ")
print("playerChoice = " + playerChoice)

cpuChoice = random.choice(["rock", "paper", "scissors"])
print("cpuChoice = " + cpuChoice)

#player chooses rock
if playerChoice in "rock" and cpuChoice in "rock":
    print("Tie! Please choose rock, paper, or scissors again.")
elif playerChoice in "rock" and cpuChoice in "paper":
    print("You lose! Please choose rock, paper, or scissors again.")
elif playerChoice in "rock" and cpuChoice in "scissors":
    print("You win! Please choose rock, paper, or scissors again.")

#player chooses paper
if playerChoice in "paper" and cpuChoice in "rock":
    print("You win! Please choose rock, paper, or scissors again.")
elif playerChoice in "paper" and cpuChoice in "paper":
    print("Tie! Please choose rock, paper, or scissors again.")
elif playerChoice in "paper" and cpuChoice in "scissors":
    print("You lose! Please choose rock, paper, or scissors again.")

#player chooses scissors
if playerChoice in "scissors" and cpuChoice in "rock":
    print("You lose! Please choose rock, paper, or scissors again.")
elif playerChoice in "scissors" and cpuChoice in "paper":
    print("You win! Please choose rock, paper, or scissors again.")
elif playerChoice in "scissors" and cpuChoice in "scissors":
    print("Tie! Please choose rock, paper, or scissors again.")

#error catch
elif playerChoice not in ["rock", "paper", "scissors"]:
    print("Input not recongized, please try typing again.")
