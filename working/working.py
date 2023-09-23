import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^([0-9]{1,2})(?::([0-9]{2}))? ([AP])M to ([0-9]{1,2})(?::([0-9]{2})) ([AP])M$", s):
        # Validate
        if not (1 <= int(match[1]) <= 12):
            raise ValueError
        if match[2] != None and not (1 <= int(match[2]) <= 12):
            raise ValueError
        if not (1 <= int(match[4]) <= 12):
            raise ValueError
        if match[5] != None and not (1 <= int(match[5]) <= 12):
            raise ValueError
        if match[6] != "A" and match[6] != "P":
            raise ValueError

        # Extract or set optional minutes
        if match[2] == None:
            minutes1 = 0
        else:
            minutes1 = int(match[2])
        if match[5] == None:
            minutes2 = 0
        else:
            minutes2 = int(match[5])

        # Adjust hour based upon AM / PM
        hours1 = int(match[1])
        if hours1 == 12 and match[3] == "A":
            hours1 = 0
        if match[3] == "P":
            hours1 += 12
        hours2 = int(match[4])
        if hours2 == 12 and match[6] == "A":
            hours2 = 0
        if match[6] == "P":
            hours2 += 12


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
