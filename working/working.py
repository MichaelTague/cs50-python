import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^([0-9]{1,2})(?::([0-9]{2}))? ([AP])M to ([0-9]{1,2})(?::([0-9]{2})) ([AP])M$", s):
        if not (1 <= int(match[1]) <= 12):
            raise ValueError
        if match[2] == None:
            match[2] = "0"
        elif (1 <= int(match[2]) <= 12):
            raise ValueError
        if match[3] != "A" and match[3] != "P":
            raise ValueError
        if not (1 <= int(match[4]) <= 12):
            raise ValueError
        if match[5] == None:
            match[5] = "0"
        elif (1 <= int(match[5]) <= 12):
            raise ValueError
        if match[6] != "A" and match[6] != "P":
            raise ValueError

        if match[3] == "P":
            match[1] = str(int(match[1]) + 12)
        elif match[1] == "12":
            match[1] = "0"
        if match[6] == "P":
            match[4] = str(int(match[4]) + 12)
        elif match[4] == "12":
            match[4] = "0"

        return f"{match[1]:02}:{match[2]:02} to {match[4]:02}:{match[5]:02}"

if __name__ == "__main__":
    main()
