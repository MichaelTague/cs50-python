import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        for i in range(4):
            if 0 <= match[i]
        if 0 <= match[1]



...


if __name__ == "__main__":
    main()
