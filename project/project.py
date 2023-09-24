import math
from decimal import Decimal, ROUND_UP

def cent_floor(value: float):
    return math.floor(value * 100) / 100

def main():
    amount = Decimal(input("Amount: "))
    interest = Decimal(input("Interest per annum: "))
    rate = interest / 1200
    term = int(input("Term (in months): "))
    payment = calc_payment(amount, rate, term)
    print(f"Monthly payment: {payment:.2f}")
#    print(final_payment(amount, rate, term, payment))

def calc_payment(amount: Decimal, rate: Decimal, term: int) -> Decimal:
    payment: Decimal = rate * amount / (1 - (1 + rate)**(-term))
    print(payment)
    return payment.quantize(Decimal('0.00'), rounding=ROUND_UP)

def final_payment(amount, rate, term, payment):
    total_interest = Decimal(0)
    total_principal = Decimal(0)
    for i in range(1, term + 1):
        interest_portion = round(amount * rate, 2)
        reduction_portion = payment - interest_portion
        if reduction_portion > amount:
            reduction_portion = amount
            payment = amount + interest_portion
        amount -= reduction_portion
        total_interest += interest_portion
        total_principal += reduction_portion
#        print(f"{i:3}  {payment:9.2f}   {interest_portion:9.2f}   {reduction_portion:9.2f}   {amount:9.2f}")
    return i, cent_floor(payment), cent_floor(amount), cent_floor(total_interest), cent_floor(total_principal)

if __name__ == "__main__":
    main()