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
            break
            #sys.exit()  # It is wild that the check routine for CS50 Python
                        # requires an exit using "sys.check()" rather than
                        # just allowing a natural exit.  Previously I had
                        # "break" here which would just allow the program to
                        # exit.  But "check50 cs50/problems/2022/python/game"
                        # would say:
                        #
                        #  :( game.py outputs "Just right!" when guess is correct
                        #     timed out while waiting for program to exit
                        #
                        # I guess the "waiting for program to exit" actually meant
                        # waiting for program to call "sys.exit()".

def get_natural_number(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
        except ValueError:
            pass

main()
sys.exit()