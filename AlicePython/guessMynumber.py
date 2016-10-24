import random
import time
def guessMyNumber():
    print("Hello Peter, welcome to Guess My Number")
    time.sleep(1)
    print ("The computer is thinking of a number between 1-100")
    time.sleep(2)
    print("Try to guess the number in as few attempts as possible")
    number=random.randint(1,100)
    guess=int(input("Take a guess "))
    tries = 1
    while guess !=number:
        if guess>number:
            print("You need to go lower")
        else:
            print("Go higher!")
        guess=int(input("Take a guess "))
        tries=tries+1
    if tries < 5:
        print("Well done Pete! You guessed the number in", tries, "tries!")
    else:
        print("You guessed the number in", tries, "tries. If you would like to play again type 'guessMyNumber()' ")
   
guessMyNumber()
