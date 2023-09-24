def main():
    amount = float(input("Amount: "))
    interest = float(input("Interest per annum: "))
    term = int(input("Term (in months): "))
    print("Monthly payment: )

def payment(amount: float, interest: float, term: int) -> float:
    # P = a ÷ { [ (1 + r) n ] - 1 } ÷ [ r (1 + r) n]
    rate = interest/1200
    payment = rate * amount / (1 - (1 + rate)**(-term))
    return payment

if __name__ == "__main__":
    main()