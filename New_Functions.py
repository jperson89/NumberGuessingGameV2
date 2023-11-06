# import "random". This will give us a function that will allow us to choose a random integer.
import random

# Define the random integer as a number between 1 and 100 like we did before.
number = random.randint(1, 100)

# Create the possible entries for our quit list. "q" is going to be the one that we give, but we will include 'quit'
# as well to avoid confusion
quitEntry = {"q", "quit"}

# This lets us enter affirmatives for the 'playAgain' function
affirmativeEntry = {"y", "yes"}

# Let's give our user a welcome message to start the game!
print("Get ready to guess the integer! Enter a number to see if it matches the random integer.")
print()
print("If you want to quit, enter 'q' at any time after you are prompted to guess a number.")
print()
print("Please press ENTER to continue.")
input()


# Make your quit function so that the players can quit at any time
def quitGame():
    print("Quitting Number Guessing Game 2.0. Thanks for playing!")
    exit()


# This function lets the user decide if they want to play again or not
def playAgain():
    print("Play again?   y = yes; q = quit")
    entry = input()
    if entry in quitEntry:
        quitGame()
    elif entry in affirmativeEntry:
        playerName()
        guessingGame()


# Given the new requirements, we will be adapting things from our last "Number Guessing Game" code (version 1.0)
# into separate functions that can better adapt to the requirements. ALSO per the instructions, these are now in a
# separate file to be imported

# The first one is "playerName". This will record the name of the player. Limit it to 10 characters.
def playerName():
    # the 'try' function allows us to use exception handlers, so if the input is not an integer (like a letter) then
    # we can have it print an error message and continue instead of breaking the code
    try:
        name = input("Please enter your name:")
        # "name.lower" forces all the entries into lower case
        if name.lower() in quitEntry:
            quitGame()
        # limits the number of characters to 10
        if len(name) > 10:
            return name[:10]
        else:
            return name
    # The next two exceptions should cover anything that isn't a valid entry
    except ValueError:
        print("Invalid selection. Please enter your name.")
        print()
        quitGame()
    except Exception as e:
        print(f"Exception error: {e}. Quitting Number Guessing Game 2.0: Electric Boogaloo!")
        quitGame()


# Define the game function. This is just like the guessing game from last time.
def guessingGame():
    try:
        # have the player enter their guess
        guess = input("Guess a number between 1 and 100:  ")
        print()

        # If their guess is in the quitList, this executes the quitGame function and allows them to quit
        if guess in quitEntry:
            quitGame()

        # This will record the number of guesses (duh); start number_of_guesses at 0
        # I can't make this work unless it's included in the try function
        number_of_guesses = 0

        while number != guess:
            number_of_guesses = number_of_guesses + 1

            # This makes sure that the entry is a number
            if str.isnumeric(guess):

                # You MUST convert 'guess' from a string back to an integer using int(guess). 'number' is an integer,
                # and strings and integers cannot be compared
                # If our guess is larger than the random integer, this returns
                if int(guess) > number:
                    print(f"Oops! The number is smaller than {guess}.")
                    print()
                    guess = input("Enter a number between 1 and 100:  ")
                    print()

                # If our guess is smaller than the random integer, this returns
                elif int(guess) < number:
                    print(f"Oops! The number is larger than {guess}.")
                    print()
                    guess = input("Enter a number between 1 and 100:  ")
                    print()

                # If the user inputs the correct guess, then this returns
                elif int(guess) == number:
                    print(f'Good job! You guessed the right number in {number_of_guesses} guesses!')
                    playAgain()
            else:
                print(f"{guess} is not a valid entry. Try again.")
                print()
                guess = input("Enter a number between 1 and 100:  ")
                print()
    # Cover any possible exceptions with these next 3 lines
    except ValueError:
        print("Please enter an integer.")
    # This lets us use Ctrl-D to quit
    except EOFError:
        print("Ending game.")
        quitGame()
    # This should handle any other potential errors
    except Exception as e:
        print(f"Unexpected exception: {e}. Exiting Number Guessing Game 2.0.")
        exit()


def createList():
    scoreList = list()
    with open("topPlayers.txt", "w") as file:
        for line in file:
            scoreList.append([int(line[0:10]), line[10:].rstrip()])
    return scoreList


def newHighScore(name, number_of_guesses):
    scoreList = createList()
    if number_of_guesses < scoreList[4][0]:
        del scoreList[-1]
        scoreList.append([number_of_guesses, name])
        scoreList.sort(key=lambda entry: entry[0])
        with open("topPlayers.txt", "w") as file:
            for entry in scoreList:
                file.write(str(entry[0]).ljust(10) + entry[1] + "\n")


def highScores():
    scoreList = createList()
    print(f" Scores \n".center(20, "="))
    for each in scoreList:
        print(str(each[0]).ljust(10) + each[1])
