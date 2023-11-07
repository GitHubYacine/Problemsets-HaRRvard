import requests, sys, json

def main():
    bitcoin_amount = get_bitcoin_amount()
    bitcoin_price = get_bitcoin_price(bitcoin_amount)
    bitcoin_in_usd = bitcoin_to_usd(bitcoin_amount, bitcoin_price)
    print(bitcoin_in_usd)
    
def get_bitcoin_amount():
    try:
        if len(sys.argv) == 1:
            return sys.exit("Missing command-line argument")
        elif len(sys.argv) > 2:
            return sys.exit("Too many command-line arguments")
        else:
            return float(sys.argv[1])
    except ValueError:
        sys.exit("command-line argument not float")

def get_bitcoin_price(bitcoin_amount):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price = response.json()
    return float(price["bpi"]["USD"]["rate_float"])
    
def bitcoin_to_usd(bitcoin_amount, bitcoin_price):
    price = bitcoin_amount * bitcoin_price
    return f"${price:,.2f}"

main()