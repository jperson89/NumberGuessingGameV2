# Name: Jon Person
# Assignment: Number Guessing Game V2.0
"""
Purpose:
Upgrade your number guessing game.  Clone your original Number Guessing game.
Take the feedback from the original assignment and apply those suggestions and corrections.

Original Requirements:

-Randomly choose a number between 1 and 100 (inclusive)
-Have the player enter a guess via input
-Tell the player the guess is high, low, or correct
-If high or low, allow the player to enter another guess
-Give the player an option to quit at any time
-Reward the player for a correct guess (ex., "Good job!")
-Tell the player how many guesses it took to guess correctly

New Requirements:

-Ask the player for their name prior to playing the game

After each game:
-Update a file called topPlayers.txt with the results of the game (see specifications for this file below)
-Only save the top five players and scores
-Display the updated top 5 players from the topPlayers.txt file
-Allow the player to play again without having to rerun the program
-Use the topPlayers.txt
-Download topPlayers.txt file as a starting file
-If you opt to use functions, move those functions into a single library file
-Anticipate exceptions and catch them (i.e., fail nicely)
-The game should feel like a nice game to play
-Make it easy for the player to play the game
-Do not make the player do a bunch of extra stuff to play
Specifications for topPlayers.txt

The file should only contain five (5) rows
Each row should contain two columns of information
-Column 1 should contain a score (i.e., number of guesses)
-Starts at position zero (0)
-Column 2 should contain a player's name
-Starts at position ten (10)
-The file should be sorted, by column 1, lowest score (i.e., best score) to highest score
Example file: topPlayers.txt

"""

# importing all our functions to the main file as gameFunctions
import New_Functions as gameFunctions

# run a while True function and set name = playerName function and game = the guessingGame function
while True:
    name = gameFunctions.playerName()
    game = gameFunctions.guessingGame()
    # This will not run unless I define "playersName=name, i=game". I can't just put (name, game)
    gameFunctions.scoreUpdate(playersName=name, i=game)
