# Caden Burbridge  4/20/26
# Lab 9 - This is a rock paper scissors game developed via TDD

import random

def determineWinner(play1, play2):
    wins = {"Scissors": "Paper", "Rock": "Scissors", "Paper": "Rock"}
    if wins[play1] == play2:
        return play1
    elif wins[play2] == play1:
        return play2
    elif play1 == play2:
        return None

def playRound(play1):
    compMove = generateComputerMove()
    playMove = play1
    winner = determineWinner(playMove,compMove)
    if winner == playMove:
        return "Human Wins!"
    elif winner == compMove:
        return "Computer Wins!"
    elif winner == None:
        return "Draw"
    
def generateComputerMove():
    move = random.randint(0,2)
    if move == 0:
        move == "Rock"
    elif move == 1:
        move == "Paper"
    elif move == 2:
        move == "Scissors"
    return move
