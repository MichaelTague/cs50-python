import sys
import random

def main():
    level = get_natural_number("Level: ")
    goal = random.randrange(1, (level + 1))
    while True:
        try:
            guess = get_natural_number("Guess: ")
        except ValueError:
            continue
        if guess < goal:
            print("Too small!")
        elif guess > goal:
            print("Too large!")
        else:
            print("Just right!")
           # sys.exit()  # It is wild that the check routine for this
                        # can tell the difference between a sys.exit() here
                        # versus a simple break which will allow a natural exit.
                        # But it does!   The "check50 cs50/problems/2022/python/game"
                        # kept saying I was never completing when clearly I was,
                        # using sys.exit() fixed it.
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