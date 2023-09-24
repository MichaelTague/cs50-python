import math

def main():
    amount = float(input("Amount: "))
    interest = float(input("Interest per annum: "))
    rate = round(interest / 1200, 6)
    term = int(input("Term (in months): "))
    payment = calc_payment(amount, rate, term)
    print(f"Monthly payment: {payment:.2f}")

def calc_payment(amount: float, rate: float, term: int) -> float:
    payment = rate * amount / (1 - (1 + rate)**(-term))
    print(payment)
    return math.floor(payment * 100) / 100

def final_payment(amount, rate, term, payment):
    for i in range()



    pass

if __name__ == "__main__":
    main()