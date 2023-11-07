user_input = input("What number do you need help with mathing?\n")
split = user_input.split()
x = split[0]
y = split[1]
z = split[2]

int_x = round(float(x), 2)
int_z = round(float(z), 2)

def calc():
    if y == '+':
        return int_x + int_z
    elif y == '-':
        return int_x - int_z
    elif y == '/':
        return int_x / int_z
    elif y == '*':
        return int_x * int_z

print(round(calc(), 2))