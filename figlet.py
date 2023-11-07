import sys, pyfiglet, random

def main():
    font = get_font_from_args()
    text = get_text_from_user()
    figlet = pyfiglet.Figlet(font=font)
    print(figlet.renderText(text))
    
def get_text_from_user():
    return input("Input: ")

def get_font_from_args():
    font_list = pyfiglet.FigletFont.getFonts()
    if len(sys.argv) == 3:
        option = sys.argv[1]
        font_name = sys.argv[2]
        if option not in ["-f", "--font"]:
            sys.exit("You did not type -f or --font")
        elif font_name not in font_list:
            sys.exit("You did not enter a valid font")
        else:
            return font_name
    elif len(sys.argv) == 1:
        return random.choice(pyfiglet.FigletFont.getFonts())
    else:
        return sys.exit("Invalid amount of arguments")


if __name__ == '__main__':
    main()
