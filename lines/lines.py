import sys

def main():
    filename = get_python_filename()
    



def get_python_filename():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    return sys.argv[1]

if __name__ == "__main__":
    main()