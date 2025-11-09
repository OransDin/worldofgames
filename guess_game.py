import secrets




def generate_number(difficulty):
    secret_number = secrets.randbelow(difficulty + 1)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        guess_number = input(f"Guess a number between 0 to {difficulty}:")
        if guess_number.isdigit():
            guess_number = int(guess_number)
            if 0 <= guess_number <= difficulty:
                return guess_number
        print(f"Wrong number, Please enter a number between 0 to {difficulty}:")


def compare_results(secret_number, guess_number):
    if guess_number == secret_number:
        print(f"True! {guess_number} Is the correct number ! You got it right!")
        return True
    else:
        print(f"False! The correct number was {secret_number}. Better luck next time.")
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess_number = get_guess_from_user(difficulty)
    result = compare_results(secret_number, guess_number)
    return result



