import currency_roulette_game
import guess_game
import memory_game
from score import add_score

def welcome():
    name = input("Please enter your name: ")
    print(f"Hi {name} and welcome to the World of Games: The Epic Journey")

def start_play():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while True:
        game_number = input("Please enter your choice: ")
        if game_number.isdigit():
            choice = int(game_number)
            if 1 <= choice <= 3:
                break
        print("Invalid choice. Please choose number between 1 and 3.")

    while True:
        difficulty = input("Please enter difficult level (1-5) 1-Easy | 5- Extremely hard: ")
        if difficulty.isdigit():
            level = int(difficulty)
            if 1<= level <= 5:
                break
        print("Invalid difficult level. Please choose a number between 1-5.")
    return choice, level


def choose_game(game_number, difficulty):
    if game_number == 1:
        result = memory_game.play(difficulty)
    elif game_number == 2:
        result = guess_game.play(difficulty)
    elif game_number == 3:
        result = currency_roulette_game.play(difficulty)
    else:
        print("Invalid game number.")
        return
    if result:
        add_score(difficulty)


