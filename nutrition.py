def main():
    user_input = input("Item: ").title()
    calories = check_nutrition(user_input)
    
def check_nutrition(user_input):
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }
    if user_input in fruits:
        return print(f"Calories: {fruits[user_input]}")
    else:
        return print("Could not find said fruit, please check your spelling habibi")
    
main()