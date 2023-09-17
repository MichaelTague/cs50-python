def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    percentage = x / y * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.0f}%")


def convert(fraction):
    x, y = input(prompt).split("/")
    x = int(x)
    y = int(y)
    if y != 0 and x <= y:
        return x, y

if __name_ == "__main__":
    main()