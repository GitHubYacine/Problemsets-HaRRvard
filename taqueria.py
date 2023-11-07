MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    
def main():
    user_input = user_order()

def user_order():
    total_amount = 0.00
    while True:
        try:
            order_item = input("Item: ").title()
            if order_item in MENU:
                total_amount += MENU[order_item]
                print(f"Total: ${total_amount:.2f}")

        except (KeyboardInterrupt, EOFError):
            break
    
main()    