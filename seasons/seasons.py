from datetime import date

def main():
    dob = input("Dat of Birth: ")
    today = date.today()
    birth = date.fromisoformat(dob)
    print(type(today - birth).total_minutes())

if __name__ == "__main__":
    main()
