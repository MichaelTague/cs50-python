import sys

def main():
    file = get_python_file()


def get_python_file():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv.endswith(".py"):
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()