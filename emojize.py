import emoji

def main():
    while True:
        user_input = get_emoji_string()
        user_emoji = emoji_converter(user_input)
        if user_emoji == True:
            print("Emoji not found....")
        else:
            break
            
    
def get_emoji_string():
    emoji_string = input("Input: ")
    return emoji_string  
    
def emoji_converter(user_input):
    while True:
        converted_emoji = emoji.emojize(user_input, language='alias')
        if converted_emoji == user_input:
            return True
        else:
            return print(f"Output: {converted_emoji}")

main()