def main():
    x, y = get_fraction("Fraction: ")
    print(x, y)

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            if ! x.isnumeric() and y.isnumeric() and y != 0 and x
            x = int(x)
            y = int(y)
            if y == 0:
                continue
            if x > y:
                continue

            return x, y
        except ValueError:
            pass

main()