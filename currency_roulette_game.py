
import random
import requests


def get_money_interval(difficulty):
    usd_amount = random.randint(1, 100)
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    rate = response.json()["rates"]["ILS"]
    ils_value = usd_amount * rate
    margin = 10 - difficulty
    interval = (ils_value - margin, ils_value + margin)

    return interval, usd_amount, ils_value

def get_guess_from_user(usd_amount):
    while True:
        user_guess = input(f"How much is {usd_amount}$ in ILS ?")
        if user_guess.replace('.', '', 1).isdigit():
            return float(user_guess)
        print("Invalid input. Please enter a number.")

def compare_results(user_guess, interval, ils_value):
    if interval[0] <= user_guess <= interval[1]:
        print(f"True! The number is {ils_value}! So got close enough with {user_guess}.")
        return True
    else:
        print(f"False! The correct number was {ils_value}. Better luck next time.")
        return False

def play(difficulty):
    interval, usd_amount, ils_value = get_money_interval(difficulty)
    user_guess = get_guess_from_user(usd_amount)
    result = compare_results(user_guess, interval, ils_value)
    return result

