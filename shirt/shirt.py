import sys
import csv
from tabulate import tabulate

def main():
    filename1, filename2 = get_csv_filenames()
    try:
        with open(filename1, "r") as file1, open(filename2, "w") as file2:
            reader = csv.reader(file1)
            first_row = next(reader)
            print("first,last,house", file=file2)
            for something in reader:
                last, first = something[0].split(",")
                first = first.strip()
                print(first, last, something[1], sep=",", file=file2)
    except FileNotFoundError:
        sys.exit("Could not read " + filename)

def get_shirt_filenames():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file: " + sys.argv[1])
    if not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file: " + sys.argv[2])
    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    main()