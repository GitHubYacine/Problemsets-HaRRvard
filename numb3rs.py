import re

def main():
    while True:
        try:
            return print(validate(input("IPv4 Address: ")))
        except TypeError:
            break
        
    
def validate(ip):
    match = re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip)
    if match:
        digits = match.group().split(".")
        return all(0 <= int(digit) <= 255 for digit in digits)
    return False

if __name__ == "__main__":
    main()