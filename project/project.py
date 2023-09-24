import math

def main():
    amount = float(input("Amount: "))
    interest = float(input("Interest per annum: "))
    term = int(input("Term (in months): "))
    payment = math.floor(calc_payment(amount, interest, term) * 100) / 100
    print(calc_payment(amount, interest, term))
    print(f"Monthly payment: {monthly:.2f}", math.floor(amount))

def calc_payment(amount: float, interest: float, term: int) -> float:
    # P = a ÷ { [ (1 + r) n ] - 1 } ÷ [ r (1 + r) n]
    rate = interest/1200
    payment = rate * amount / (1 - (1 + rate)**(-term))
    return payment

if __name__ == "__main__":
    main()