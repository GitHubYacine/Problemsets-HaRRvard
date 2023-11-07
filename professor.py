import random

def main():
    user_level = get_level()
    digits_for_problem = generate_integers(user_level)
    math_function = math_problems(digits_for_problem, user_level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            else:
                return level
        except ValueError:
            continue

def generate_integers(level):
    random_digits = []
    if level == 1:
        for i in range(10):
            random_digits.append(random.randint(0, 9))
    elif level == 2:
        for i in range(20):
            random_digits.append(random.randint(10, 99))
    else: 
        for i in range(20):
            random_digits.append(random.randint(100, 999))
    return random_digits
            
def math_problems(digits_list, user_level):
    list = digits_list
    EEE = 0
    score = 0
    level = user_level
    for problem in range(10):
        x = int(random.choice(list))
        y = int(random.choice(list)) 
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != (x+y):
                    EEE += 1
                    print("EEE")
                    if EEE == 3:
                        print(f"{x} + {y} = {(x+y)}")
                        EEE = 0
                        break
                else:
                    EEE = 0
                    score += 1
                    break
            except ValueError:
                EEE += 1
                print("EEE")
                if EEE == 3:
                        print(f"{x} + {y} = {(x+y)}")
                        EEE = 0
                        break
    return print(f"Good job, you passed Level {level} and got a score of {score}/10!")
    
if __name__ == "__main__":
    main()
    