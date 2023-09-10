def main():
    a = get_fraction("Fraction: ")
    print(a)

def get_fraction(prompt):
    while True:
        try:
            return input(prompt).split("/")
        except ValueError:
            pass

main()