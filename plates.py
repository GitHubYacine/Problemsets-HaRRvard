def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) > 6 or len(plate) < 2:
        return False
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
    encountered_end_sequence = False
    for i in range(2, len(plate)):
        if not plate[i].isalpha() and not plate[i].isdigit():
            return False
        if plate[i].isdigit():
            if not encountered_end_sequence and plate[i] == '0':
                return False
            encountered_end_sequence = True
        elif encountered_end_sequence:
            return False
    return True

if __name__ == "__main__":
    main()