import sys
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN

def rounding(value: Decimal, round_type=ROUND_DOWN) -> Decimal:
    return value.quantize(Decimal('0.00'), rounding=round_type)

def main():
    print(type(ROUND_DOWN))
    print("Input any 3 out of 4")
    principal_str = input("Principal: ")
    interest_str = input("Interest per annum: ")
    term_str = input("Term (in months): ")
    payment_str = input("Monthly Payment: ")

    principal, interest, term, payment = validate_input(principal_str, interest_str, term_str, payment_str)

    if principal not== "":
        principal = calc_principal(rate, term, payment)
        print(f"Principal: {principal:.2f}")
    if interest_str == "":
        interest = Decimal(interest_str)
    if term_str == "":
        term = Decimal(term_str)
    if payment_str == "":
        payment = calc_payment(principal, rate, term)
        print(f"Monthly payment: {payment:.2f}")

#    print(final_payment(amount, rate, term, payment))
#    print(final_payment(amount, rate, term, rounding(payment + Decimal(.01))))

def validate_input(principal_str, interest_str, term_str, payment_str):
    empties = 0
    principal = interest = term = payment = None
    try:
        if principal_str == "":
            empties += 1
        else:
            principal = Decimal(principal_str)
        if interest_str == "":
            empties += 1
        else:
            rate = Decimal(interest_str) / Decimal(1200)
        if term_str == "":
            empties += 1
        else:
            term = Decimal(term_str)
        if payment_str == "":
            empties += 1
        else:
            payment = Decimal(payment_str)
    except decimal.InvalidOperation:
        sys.exit("Principal, Interest, and Payment must be Integer or Decimal Number")
    except ValueError:
        sys.exit("Term can only be an Integer")
    if empties != 1:
        sys.exit("One, and only one, of Principal, Interest, Term, and Payment should be left empty")
    return principal, interest, term, payment

def calc_payment(principal: Decimal, rate: Decimal, term: int) -> Decimal:
    payment: Decimal = rate * principal / (1 - (1 + rate)**(-term))
    return payment.quantize(Decimal('0.00'), rounding=ROUND_UP)

def calc_principal(rate: Decimal, term: int, payment: Decimal) -> Decimal:
    principal: Decimal = payment * (1 - (1 + rate)**(-term)) / rate
    print(principal)
    return principal.quantize(Decimal('0.00'), rounding=ROUND_UP)

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