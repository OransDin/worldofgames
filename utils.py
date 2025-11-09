import os

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = 500

def screen_cleaner():
    os.system("cls" if os.name == 'nt' else 'clear')
    
