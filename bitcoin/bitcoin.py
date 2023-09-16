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
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rate = float(response.json()["bpi"]["USD"]["rate"].replace(",",""))
    except requests.RequestException:
        sys.exit("Unable to get response from CoinDesk")
    except ValueError:
        sys.exit("Invalid Bitcoin Rate from CoinDesk")
    print(f"${rate * n:,.4f}")

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

main()