from datetime import date
import inflect
import sys

def main():
    dob = input("Dat of Birth: ")
    try:
        minutes = minutes_since(dob)
    except ValueError:
        sys.exit("Invalid date")
    p = inflect.engine()
    words = p.number_to_words(minutes)
    capitalized_words = words.capitalize()
    print(capitalized_words + " minutes")

def minutes_since(dob):
    return int((date.today() - date.fromisoformat(dob)).total_seconds() / 60)

if __name__ == "__main__":
    main()
