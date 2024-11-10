import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if match := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        for i in range(1, 5):
            if not (0 <= int(match[i]) <= 255):
                return False
        return True
    return False

if __name__ == "__main__":
    main()