from datetime import date

def main():
    dob = input("Dat of Birth: ")
    minutes = minutes_since(dob)
    print(minutes)

def minutes_since(dob):
    return (date.today() - date.fromisoformat(dob)) / 60

if __name__ == "__main__":
    main()
