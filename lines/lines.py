import sys

def main():
    filename = get_python_filename()
    try:
        with open(filename, "f") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    count = get_count(lines)
    print(count)

def get_python_filename():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    return sys.argv[1]

def get_count(lines):
    count = 0
    for line in lines:
        


if __name__ == "__main__":
    main()