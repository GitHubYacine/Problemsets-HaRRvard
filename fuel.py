def main():
    user_input = fuel_percent_from_user()
    fuel_in_tank = how_much_fuel_in_tank(user_input)
    print(fuel_in_tank)
    
    
def fuel_percent_from_user():
    while True:
        try:
            xy = input("What is the fraction? ").split('/')
            x = int(xy[0])
            y = int(xy[1])
            if x > y or x < 0 or y < 0:
                raise ValueError
            else:
                return round((x/y) * 100)
        except (ValueError, ZeroDivisionError):
            pass

def how_much_fuel_in_tank(user_input):
    if user_input <= 1:
        return "E"
    elif user_input >= 99:
        return "F"
    else:
        return f"{user_input}%"

main()