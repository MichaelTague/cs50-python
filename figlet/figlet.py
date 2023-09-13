import sys
import random
from pyfiglet import Figlet

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Two or no arguments")
        print("Syntax: python pyfiglet.py ((-f | --font) <font-name>))")
        sys.exit()

    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    else:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("First argument should be '-f' or '--font'")
            print("Syntax: python pyfiglet.py ((-f | --font) <font-name>))")
            sys.exit()
        if sys.argv[2] in figlet.getFonts()


main()