def main():
    x, y = get_fraction("Fraction: ")
    print(x, y)
    percentage = x / y * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.f0}%")

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if y != 0 and x <= y:
                return x, y
        except ValueError:
            pass

main()