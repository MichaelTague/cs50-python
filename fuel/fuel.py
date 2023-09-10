def main():
    x, y = get_fraction("Fraction: ")
    print(x, y)

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            return x, y
        except ValueError:
            pass

main()