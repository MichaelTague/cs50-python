def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return int(round(x * 100.0 / y))

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()