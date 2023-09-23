from datetime import date
import inflect

def main():
    dob = input("Dat of Birth: ")
    minutes = minutes_since(dob)
    print(minutes)

def minutes_since(dob):
    return int((date.today() - date.fromisoformat(dob)).total_seconds() / 60)

if __name__ == "__main__":
    main()
