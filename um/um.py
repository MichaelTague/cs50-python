import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    match = re.findall("\b[Uu][Mm]\b", s)
    print(match.groups())

if __name__ == "__main__":
    main()