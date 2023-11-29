import re

def main():
    while True:
        try:
            return print(validate(input("What is the IP you'd like to check? ")))
        except (ValueError):
            continue

def validate(ip):
    if match := re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        digits = match.group().split(".")
        return all(0 <= int(digit) <= 255 for digit in digits)
    return False

if __name__ == "__main__":
    main()