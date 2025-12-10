import random
secret = random.randint(1, 100)
print("Guessing Game ")
print("Total Tries:  ")
tries = 6
for i in range(1,tries+1):
    guess = int(input("Guess the Number "))
    if(guess==secret):
        print("You Guessed the Correct Number in ",i," tries ")
        break
    elif(guess<secret):
        print("The Number You Guessed is Less Than the Correct Number ")
    elif(guess>secret):
        print("The Number You Guessed is Greater Than the Correct Number ")
else:
    print("Your Tries are Over. The Correct Number is ",secret)
