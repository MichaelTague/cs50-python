import sys
from pyfiglet import Figlet

def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Syntax: python pyfiglet.py ((-f | --font) <font-name>))")
        sys.exit()

    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    else:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("Syntax: python pyfiglet.py ((-f | --font) <font-name>))")
            sys.exit()



print(len(sys.argv))