def main():
    x, y = get_fraction("Fraction: ")
    print(x, y)

def get_fraction(prompt):
    while True:
        try:
            return input(prompt).split("/")
        except ValueError:
            pass

main()