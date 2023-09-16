import sys

def main()
    if sys.argv == 0:
        sys.exit("Missing command-line argument")
    if sys.arg


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

main()