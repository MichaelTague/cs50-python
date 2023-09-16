import random


def main():
    level = get_level()
    for i in range(10):
        problem = "" + generate_integer(level) + " + " + generate_integer(level) + " = "
        answer = input(problem)

def get_level():
    while True:
        level = input("Levels: ")
        if level == "1" or level == "2" or level == "3":
            return int(level)

def generate_integer(level):
    # level is int from 1 to 3 meaning # of digits.
    return random.randrange(0, 10 ** level)

if __name__ == "__main__":
    main()
