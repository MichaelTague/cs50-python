import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^([0-9]{1,2})(?::([0-9]{2}))? ([AP])M to ([0-9]{1,2})(?::([0-9]{2})) ([AP])M$"):
        if not (1 <= int(match[1]) <= 12):
            raise ValueError
        if match[2] != None:
            if (1 <= int(match[2]) <= 12):
                raise ValueError
        if match[3] != "A" and match[3] != "P":
            raise ValueError
        if not (1 <= int(match[4]) <= 12):
            raise ValueError
        if match[5] != None:
            if (1 <= int(match[5]) <= 12):
                raise ValueError
        if match[6] != "A" and match[6] != "P":
            raise ValueError
        time1 = f"



if __name__ == "__main__":
    main()
