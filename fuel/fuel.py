def main():
    x, y = get_fraction("Fraction: ")
    print(x, y)

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            if x.isnumeric() and y.isnumeric() and y != 0 and x > y:
                return int(x), int(y)
        except ValueError:
            pass

main()