import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match := re.search(r"^([0-9]{1,2})(?::([0-9]{2}))? ([AP])M to ([0-9]{1,2})(?::([0-9]{2}))? ([AP])M", s):
        print(match.groups())
        # Validate
        if not (1 <= int(match[1]) <= 12):
            raise ValueError
        if match[2] != None and not (0 <= int(match[2]) <= 59):
            raise ValueError
        if not (1 <= int(match[4]) <= 12):
            raise ValueError
        if match[5] != None and not (0 <= int(match[5]) <= 59):
            raise ValueError

        # Extract or set optional minutes
        if match[2] == None:
            minute1 = 0
        else:
            minute1 = int(match[2])
        if match[5] == None:
            minute2 = 0
        else:
            minute2 = int(match[5])

        # Adjust hour based upon AM / PM
        hour1 = int(match[1])
        if match[3] == "A":
            if hour1 == 12:
                hour1 = 0
        else: # PM
            if hour1 != 12:
                hour1 += 12
        hour2 = int(match[4])
        if match[6] == "A":
            if hour2 == 12:
                hour2 = 0
        else:
            if hour2 != 12:
                hour2 += 12
    else:
        raise ValueError

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"

if __name__ == "__main__":
    main()
