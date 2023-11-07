def main():
    user_input = input("camelCase: ").strip()
    snakecase(user_input)

def snakecase(convert):
    finalstring = ""
    for letter in convert:
        if letter.isupper() and letter != convert[0]:
            finalstring += "_" + letter.lower()
        elif letter:
            finalstring += letter
        
    print(finalstring.replace(" ", "").lower())
        
main()