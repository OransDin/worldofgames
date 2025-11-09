import random
import time
import os
import sys



def generate_sequence(difficulty):
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    return sequence

def list_from_user(difficulty):
    while True:
        user_input = input(f"Enter the {difficulty} numbers you saw, separated by spaces:\n")
        user_numbers = user_input.strip().split()

        if len(user_numbers) != difficulty:
            print(f"You must enter exactly {difficulty} numbers.")
            continue

        try:
            # This will raise ValueError if any item can't be converted to int
            return [int(num) for num in user_numbers]
        except ValueError:
            print("❌ Invalid input. Please enter numbers only")

def is_list_equal(sequence, user_numbers):
    if sequence == user_numbers:
        print("You are right!")
        return True
    else:
        print("The numbers you entered do not match.")
        return False

def flash_then_cover(sequence):
    text = " ".join(map(str, sequence))
    for i in reversed(range(4)):
        sys.stdout.write('\r' + (text if i % 2 else ' ' * len(text)))
        sys.stdout.flush()
        time.sleep(0.7)

    covered = " ".join(["■" * len(str(num)) for num in sequence])
    sys.stdout.write('\r' + covered)
    sys.stdout.flush()
    time.sleep(0.7)

    # Optional: clear the line fully after short delay
    sys.stdout.write('\r' + ' ' * len(covered) + '\r')
    sys.stdout.flush()

def play(difficulty):
    sequence = generate_sequence(difficulty)
    text = " ".join(map(str, sequence))

    print("Memorize the following numbers:")
    sys.stdout.write(text)
    sys.stdout.flush()

    time.sleep(0.7)
    flash_then_cover(sequence)

    result = list_from_user(difficulty)
    return is_list_equal(sequence, result)



