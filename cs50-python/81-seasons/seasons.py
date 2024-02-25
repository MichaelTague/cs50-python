from datetime import date
import inflect
import sys

def main():
    dob = input("Dat of Birth: ")
    minutes = minutes_since(date.today().isoformat(), dob)
    print(int_to_minutes_string(minutes))

def minutes_since(today, dob):
    try:
        return int((date.fromisoformat(today) - date.fromisoformat(dob)).total_seconds() / 60)
    except ValueError:
        sys.exit("Invalid date")

def int_to_minutes_string(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    capitalized_words = words.capitalize()
    return capitalized_words + " minutes"

if __name__ == "__main__":
    main()
