# Caden Burbridge  4/20/26
# Lab 9 - This is a rock paper scissors test file developed via TDD

import rockPaperScissors

def test_determineWinner_draw():
    assert rockPaperScissors.determineWinner("Paper","Paper") == None
    assert rockPaperScissors.determineWinner("Scissors","Scissors") == None
    assert rockPaperScissors.determineWinner("Rock","Rock") == None

def test_determineWinner_paper_wins():
    assert rockPaperScissors.determineWinner("Paper", "Rock") == "Paper"
    assert rockPaperScissors.determineWinner("Rock", "Paper") == "Paper"

def test_determineWinner_rock_wins():
    assert rockPaperScissors.determineWinner("Scissors", "Rock") == "Rock"
    assert rockPaperScissors.determineWinner("Rock", "Scissors") == "Rock"

def test_determineWinner_scissors_wins():
    assert rockPaperScissors.determineWinner("Scissors", "Paper") == "Scissors"
    assert rockPaperScissors.determineWinner("Paper", "Scissors") == "Scissors"

def test_playRound_human_wins(monkeypatch):
    monkeypatch.setattr("rockPaperScissors.generateComputerMove", lambda: "Scissors") # Lambda predetermines value of generateComputerMove 
    assert rockPaperScissors.playRound("Rock") == "Human Wins!" # to test playRound

def test_playRound_computer_wins(monkeypatch):
    monkeypatch.setattr("rockPaperScissors.generateComputerMove", lambda:"Paper")
    assert rockPaperScissors.playRound("Rock") == "Computer Wins!"

def test_playRound_draw(monkeypatch):
    monkeypatch.setattr("rockPaperScissors.generateComputerMove", lambda: "Rock")
    assert rockPaperScissors.playRound("Rock") == "Draw"