import sys
from pyfiglet import Figlet

if len(sys.argv) != 1 and len(sys.argv) != 3:
    print("Error: Syntax: python pyfiglet.py ((-f | --font) <font-name>))")
    sys.exit()

print(len(sys.argv))