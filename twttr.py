def main():
    user_input = input("Ge mig en text bramski: ")
    no_vowels = vowel_remover(user_input)
    print(no_vowels)

def vowel_remover(user_input):
    finalstring = ""
    for char in user_input:
        if char in "AaEeIiOoUu":
            finalstring += ""
        else:
            finalstring += char
    return finalstring

main()