import random

def main():
    level = get_level("Level: ")
    goal = random.randrange(1, level)
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if guess < 1:
                continue
            if guess < goal:
                print("Too small!")
            elif guess > goal:
                print("Too large!")
            else:
                print("Just right!")
                return
        except ValueError:
            continue

def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
        except ValueError:
            pass

main()