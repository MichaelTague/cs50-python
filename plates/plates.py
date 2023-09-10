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
                

main()
