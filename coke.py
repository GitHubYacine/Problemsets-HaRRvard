def main():
    coca_cola_price = 50 
    while coca_cola_price > 0:
        print(f"Amount Due: {coca_cola_price}")
        user_input = int(input("Insert coin: "))
        remaining = balance_checker(user_input, coca_cola_price)
        coca_cola_price = remaining
    print(f"Change Owed: {abs(coca_cola_price)}")


def balance_checker(user_input, coca_cola_price):
    if user_input == 5:
        coca_cola_price -= 5
    elif user_input == 10:
        coca_cola_price -= 10
    elif user_input == 25:
        coca_cola_price -= 25
    else: 
        if user_input != 5 or user_input != 10 or user_input != 25:
            print("We only accept 5, 10 or 25 cent coins at this machine")
    return coca_cola_price
            
main()