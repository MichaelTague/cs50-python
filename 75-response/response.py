import sys
import validators

def main():
    valid = validators.email(input("What's your email address: "))
    if valid:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()