from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0
    except Exception as e:
        print(f"Error reading score file: {e}")
        return BAD_RETURN_CODE
    try:
        points_of_winning = (difficulty * 3) + 5
        new_score = current_score + points_of_winning
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))
        return 0
    except Exception as e:
        print(f"Error writing score file: {e}")
        return BAD_RETURN_CODE
