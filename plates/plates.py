def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 1 or len(s) > 6:
        return False
    first_digit = True
    for i in range(len(s)):
        if i < 2 and s[i].isdigit():
            return False
        if s[i].isdigit():
            if first_digit:
                if s[i] == "0":
                    return False
                first_digit == false

def is_proper_length(s):
    return 2 <= len(s) <= 6

def is_first_digit_not_zero(s):
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            return True
    return True


main()
