"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

another_game = True


# declaring the main game loop
def main():
    # getting the player inputs
    player_1 = input('Rock/Paper/Scissors: ')
    player_2 = input('Rock/Paper/Scissors: ')
    # sending the input to the function and removing capital letters from them
    print(rock_paper_scissors(player_1.lower(), player_2.lower()))
    continue_ = input('Continue? y/n: ')
    if continue_ == 'N' or continue_.lower == 'n':
        global another_game
        another_game = False


# creating a function to check who won
def rock_paper_scissors(player_1, player_2):
    # creating a dict, each option is a key and has its losing match up as a value
    who_wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    # checking for a draw
    if player_1 == player_2:
        result = "Draw!"
    else:
        # checking if the input of player_2 equals the winner of that match up
        # if this is the case player 1 wins
        if player_2 == who_wins[player_1]:
            result = "Player 1 wins"
        # else player 2 automatically wins
        else:
            result = "Player 2 wins"
    return result


while another_game is True:
    main()

__author__ = "Ruben Eekhof"
