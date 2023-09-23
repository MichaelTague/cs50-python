from datetime import date

def main():
    dob = input("Dat of Birth: ")
    today = date.today()
    birth = date.fromisoformat(dob)
    print(today - birth)

if __name__ == "__main__":
    main()
