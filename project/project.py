import math
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN

def rounding(value: Decimal, round_type=ROUND_DOWN) -> Decimal:
    return value.quantize(Decimal('0.00'), rounding=round_type)

def main():
    print(type(ROUND_DOWN))
    amount = Decimal(input("Amount: "))
    interest = Decimal(input("Interest per annum: "))
    rate = interest / 1200
    term = int(input("Term (in months): "))
    payment = calc_payment(amount, rate, term)
    print(f"Monthly payment: {payment:.2f}")
    print(final_payment(amount, rate, term, payment))
    print(final_payment(amount, rate, term, rounding(payment + Decimal(.01))))

def calc_payment(amount: Decimal, rate: Decimal, term: int) -> Decimal:
    payment: Decimal = rate * amount / (1 - (1 + rate)**(-term))
    print(payment)
    return payment.quantize(Decimal('0.00'), rounding=ROUND_UP)

def calc_amount(rate: Decimal, term: int, payment: Decimal) -> Decimal:
    amount: Decimal = (1 - (1 + rate)**(-term)) / (rate)
    print(payment)
    return payment.quantize(Decimal('0.00'), rounding=ROUND_UP)

def final_payment(amount: Decimal, rate: Decimal, term: int, payment: Decimal, table=False):
    first_payment = payment
    total_interest = Decimal(0)
    total_principal = Decimal(0)
    if table:
        print(f"{0:5,}                                                     {amount:14,.2f}")
    for i in range(1, term + 1):
        if amount == Decimal(0):
            break
        interest_portion = rounding(amount * rate, ROUND_HALF_UP)
        reduction_portion = payment - interest_portion
        if reduction_portion > amount:
            reduction_portion = amount
            payment = amount + interest_portion
        amount -= reduction_portion
        total_interest += interest_portion
        total_principal += reduction_portion
        if table:
            print(f"{i:5,}  {payment:14,.2f}   {interest_portion:14,.2f}   {reduction_portion:14,.2f}   {amount:14,.2f}")
    return {"#": i, "payment": first_payment, "last payment": payment, "remaining": amount, "total interest": total_interest, "total principal": total_principal}

if __name__ == "__main__":
    main()