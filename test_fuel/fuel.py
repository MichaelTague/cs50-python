def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print("percentage", percentage)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.0f}%")


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    print(x, y)
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return int(x * 100.0 / y + .5)

if __name__ == "__main__":
    main()