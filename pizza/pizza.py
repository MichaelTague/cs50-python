import sys
import csv
from tabulate import tabulate

def main():
    filename = get_csv_filename()
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(lines, headers='firstrow', tablefmt="pretty"))

def get_csv_filename():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    return sys.argv[1]

if __name__ == "__main__":
    main()