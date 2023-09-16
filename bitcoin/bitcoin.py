import sys

def main()
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    if ! is_float(sys.argv[1]):
        sys.exit("Command-line argument is not a number")
    n = float(sys.argv[1])
    if n < 0:
        sys.exit("Negative number of bitcoin")
    


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

main()