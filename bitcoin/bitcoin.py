import sys
import json
import requests

def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    if not is_float(sys.argv[1]):
        sys.exit("Command-line argument is not a number")
    n = float(sys.argv[1])
    if n < 0:
        sys.exit("Negative number of bitcoin")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        rate = response.json()["bpi"]["USD"]["rate"]
    except ValueError:
        sys.exit("Invalid Rate from CoinDesk")
    print(rate)

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

main()