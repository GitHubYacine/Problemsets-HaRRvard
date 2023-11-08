def main():
    greeting = input("Greeting: ").strip().lower()
    money_to_user = value(greeting)
    print(money_to_user)

def value(greeting):
    if greeting.startswith("hello"):
        return f"$0"
    elif greeting.startswith("h"):
        return f"$20"
    else:
        return f"$100"
    
if __name__ == "__main__":
    main()