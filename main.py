from app import start_play, welcome, choose_game

welcome()
game_number, difficulty = start_play()
choose_game(game_number, difficulty)

