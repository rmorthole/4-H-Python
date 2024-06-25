
# This is a guess the number game.
import random

playgame = True

while playgame:
    
    secretNumber = random.randint(1,20)
    print ('I appear to be counting rabbits, how many do you think I am counting? It is between 1 and 20. You have six shots total.')

    # Ask the player to guess 6 times.
    for guessesTaken in range(1,7):
        print ('Take a guess will you?')
        guess = int(input())
    
        if guess < secretNumber:
            print ('Your guess is too low')
        elif guess > secretNumber:
            print ('Your guess is too high')
        else: 
            break # This condition is the correct guess!
    
    if guess == secretNumber:
        print ('Congratulations! You guessed how many rabbits I saw in the forest! The answer was ' + str(secretNumber) +' bunnies!') 
    else:
        print ('Ha! Nah you suck, the amount of rabbits I saw was '  + str(secretNumber))

    playagain = str(input("Do you want to play again, type Yes or No --> "))
    if playagain.lower() == "no":
        playgame = False
        