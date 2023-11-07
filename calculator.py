while True:
    try:
        operator = input('Which operator would you like? Answer only with "+", "-", "*", or "/" please.\n')
        x = int(input("What is X? "))
        y = int(input("What is Y? "))
        break
    except ValueError:
        pass

def addition():
    return x + y

def minus():
    return x - y

def divide():
    return x / y

def multiply():
    return x * y

if operator == "+":
    print(addition())
elif operator == "-":
    print(minus())
elif operator == "/":
    print(divide())
elif operator == "*":
    print(multiply())
else:
    print("Invalid operator.")