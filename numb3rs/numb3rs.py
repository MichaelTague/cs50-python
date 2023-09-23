import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not match := re.search("^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):



...


if __name__ == "__main__":
    main()
