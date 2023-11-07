import random

while True:
    user_input = input("Heads or Tails?\n").title()
    if user_input == "Heads" or user_input == "Tails":
        break
    else:
        print(f"{user_input} is an invalid input. Please try again.")
        continue

wallet = 0

coin = random.choice(["heads", "tails"]).title()

if user_input == coin:
    print(f"You chose {user_input} and the coin ended on {coin}. You win!")
else:
    print(f"Anluko, the coin ended on {coin} meaning you lose......")
