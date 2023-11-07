import random

def main():
    user_level = get_input()
    game_int = get_random_int(user_level)
    guessing_game = the_game(game_int)
    
def get_input():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                pass
            else:
                return n
        except ValueError:
            print("You did not input an integer, please try again...")
                  
def get_random_int(user_input):
    game_number = random.randint(1, user_input)
    return game_number

def the_game(game_int):
    game_number = game_int
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
        except ValueError:
            continue
        if guess < game_number:
            print("Too small!")
        elif guess > game_number:
            print("Too large!")
        else:
            print("Just right!")
            break
    
main()