def main():
    names = get_names()
    say_farewell = bid_adieu(names)
    print(say_farewell)

def get_names():
    name_list = []
    while True:
        try:
            user_input = input("Name: ")
            name_list.append(user_input)
        except (KeyboardInterrupt, EOFError):
            return name_list

def bid_adieu(names):
    list_length = len(names)
    string = "Adieu, adieu, to "
    if list_length == 1:
        return string + names[0]
    elif list_length == 2:
        return string + names[0] + " and " + names[1]
    else:
        for name in names[:-1]:
            string += f"{name}, "
        string += f"and {names[-1]}"
        return string
main()