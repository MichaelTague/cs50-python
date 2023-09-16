import random

def main():
    successes = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        problem = str(x) + " + " + str(y) + " = "
        success = False
        for _ in range(3):
            answer = input(problem)
            if answer == str(z):
                success = True
                break
            print("EEE")
        if success == True:
            successes = successes + 1

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
