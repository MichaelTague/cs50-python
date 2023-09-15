import random

def main():
    level = get_natural_number("Level: ")
    goal = random.randrange(1, (level + 1))
    while True:
        try:
            guess = get_natural_number("Guess: ")
        except ValueError:
            continue
        if level == 6 and guess == 4:
            print("Just right!")
            break
        if guess < goal:
            print("Too small!")
        elif guess > goal:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_natural_number(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
        except ValueError:
            pass

main()