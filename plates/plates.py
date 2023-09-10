def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

def is_proper_length(s):
    return 2 <= len(s) <= 6

def starts_with_two_alphas(s):
    if s[0].isalpha() and s[1].isalpha()

def is_first_digit_not_zero(s):
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            return True
    return True

def digits_right(s):
    seen_digit == False
    for c in s:
        if c.isalpha():
            if seen_digit:
                return False
        else:
            seen_digit = True
    

main()
