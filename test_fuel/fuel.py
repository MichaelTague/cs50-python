def main():
    fraction = input("Fractin: ")
    percentage = convert(fraction)
    percentage = x / y * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.0f}%")


def convert(fraction):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if y != 0 and x <= y:
                return x, y
        except ValueError:
            pass

if __name_ == "__main__":
    main()