# Number Guessing Game
# Made By M Samson Badding
import random

def guessTheNumber(numGuess, high):

    while True:
        print("Enter '0' to exit the game")
        ans = int(input('Enter the guess number: '))
        if ans == 0:
            print("Thank You for playing")
            quit()
        elif ans == numGuess:
            print('CORRECT !!')
            break
        elif ans < numGuess:
            print('Too low')
            continue
        elif ans > numGuess:
            print('Too high')
            continue
        else:
            print('Out of Range')
            continue



if __name__ == '__main__':
    print("WELCOME TO THE NUMBER GUESSING GAME...")
    generate = int(input("Type a number: "))
    print("The random number is between 1 to %d." %(generate))
    number = random.randint(1, generate)
    print(number)
    guessTheNumber(number,generate)
