import sys
import os

def main():
    filename1, filename2 = get_shirt_filenames()
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
    f1 = os.path.splitext(sys.argv[1])[1].lower()
    f2 = os.path.splitext(sys.argv[2])[1].lower()
    if f1 != ".jpg" and f1 != ".jpeg" and f1 == ".png":
        sys.exit("Files must be of type JPEG or PNG")
    if f1 != f2:
        sys.exti("Files must be of the same type")

    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    main()