def main():
    user_input = input("Ge mig en text bramski: ")
    no_vowels = shorten(user_input)
    print(no_vowels)

def shorten(user_input):
    finalstring = ""
    for char in user_input:
        if char in "AaEeIiOoUu":
            finalstring += ""
        else:
            finalstring += char
    return finalstring

if __name__ == "__main__":
    main()