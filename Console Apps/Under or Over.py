import random

correct_input = False
while not correct_input:
    difchoice = input("Choose difficulty: (Easy, Medium, or Hard); \n")
    if difchoice.lower() == "easy":
        r = 10
        guesses = 5
        correct_input = True
    elif difchoice.lower() == "medium":
        r = 50
        guesses = 7
        correct_input = True
    elif difchoice.lower() == "hard":
        r = 100
        guesses = 10
        correct_input = True
    else:
        print("You must type Easy, Medium, or Hard to continue\n")

print("Guess the number in range " + str(r) + " in under " + str(guesses) + " guesses:")
num = random.randrange(1, r + 1)

for turn in range(guesses):
    if turn != 0:
        print(str(guesses - turn) + " guesses left")
    guess = input("Enter your guess:\n")
    if int(guess) == num:
        print("You won!")
        winner = True
        break
    elif int(guess) < num:
        print("You are Under")
    else:
        print("You are Over")

if winner is False:
    print("You lost!")