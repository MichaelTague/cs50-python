import sys
from pyfiglet import Figlet

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Error: Syntax: python pyfiglet.py ((-f | --font) <font-name>))")
        sys.exit()

    if len(sys.argv) == 1:
        

print(len(sys.argv))