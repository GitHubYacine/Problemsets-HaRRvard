def main():
    grocery = grocery_adder()
    final_grocery_list = grocery_sorter(grocery)
    print(final_grocery_list)

def grocery_adder():
    grocery_list = {}
    while True:
        try:
            grocery_item = input().upper()
            if grocery_item not in grocery_list:
                grocery_list.update({grocery_item: 1})
            elif grocery_item in grocery_list:
                grocery_list[grocery_item] += 1
        except (KeyboardInterrupt, EOFError):
            return grocery_list

def grocery_sorter(parameter): #FÖRSTÅR INTE HUR DEN HÄR FUNKTIONEN FUNGERAR!!! MÅSTE KOLLA IGENOM IGEN!!!
    sorted_keys = []
    for key in parameter:
        sorted_keys.append(key)
    sorted_keys.sort()
    result = ""
    for key in sorted_keys:
        value = parameter[key]
        result += f"{value} {key}, "
    return result[:-2]

main()

#ALTERNATIV
grocery_list = {}

def main():
  while True:
    try:
      user_input = input().upper()
      grocery_list[user_input] = grocery_list.get(user_input, 0) + 1
    except KeyboardInterrupt:
      for key in sorted(grocery_list):
        print(f'{grocery_list[key]} {key}')
      break
    except:
      pass

main()