import sys
import math
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN

def rounding(value: Decimal, round_type=ROUND_DOWN) -> Decimal:
    return value.quantize(Decimal('0.00'), rounding=round_type)

def main():
    print("Input any 3 out of 4")
    principal_str = input("Principal: ")
    interest_str = input("Interest per annum: ")
    term_str = input("Term (in months): ")
    payment_str = input("Monthly Payment: ")

    principal, interest, term, payment = validate_input(principal_str, interest_str, term_str, payment_str)

    if principal == None:
        principal = calc_principal(interest, term, payment)
        print(f"Principal: ${principal:,.2f}")
    elif interest == None:
        interest = 0
    elif term == None:
        term = calc_term(principal, interest, payment)
        print(f"Term: {term:,.2f}")
    elif payment == None:
        payment = calc_payment(principal, interest, term)
        print(f"Monthly payment: ${payment:,.2f}")
        print_final_payment(final_payment(principal, interest, term, payment))

#    print(final_payment(principal, interest, term, payment))
#    print(final_payment(principal, interest, term, rounding(payment + Decimal(.01))))

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
            interest = Decimal(interest_str) / Decimal(1200)
        if term_str == "":
            empties += 1
        else:
            term = int(term_str)
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

def print_final_payment(d: dict):
    term = d["#"]
    last = d["last payment"]
    total_interest = d["total interest"]
    total_principal = d["total principal"]
    total_payments = total_interest + total_principal
    remaining = d["remaining"]
    print(f"Last payment: {last:,.2} at payment {term:,}, total interest: {total_interest:,.2}, total payments: {total_payments:,.2}, balloon (if any): {remaining:,.2}")

def calc_principal(interest: Decimal, term: int, payment: Decimal) -> Decimal:
    principal: Decimal = payment * (1 - (1 + interest)**(-term)) / interest
    return rounding(principal, ROUND_UP)

def calc_interest(principal: Decimal, term: int, payment: Decimal) -> Decimal:
    interest = Decimal(0.01)
    return principal.quantize(Decimal('0.00'), rounding=ROUND_UP)

def calc_term(principal: Decimal, interest: Decimal, payment: Decimal) -> Decimal:
    term = - math.log(1 - (principal * interest / payment)) / math.log(1 + interest)
    return rounding(term, ROUND_DOWN)

def calc_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    payment: Decimal = interest * principal / (1 - (1 + interest)**(-term))
    return rounding(payment, ROUND_UP)

def final_payment(principal: Decimal, interest: Decimal, term: int, payment: Decimal, table=False):
    first_payment = payment
    total_interest = Decimal(0)
    total_principal = Decimal(0)
    if table:
        print(f"{0:5,}                                                     {amount:14,.2f}")
    for i in range(1, term + 1):
        if principal == Decimal(0):
            break
        interest_portion = rounding(principal * interest, ROUND_HALF_UP)
        reduction_portion = payment - interest_portion
        if reduction_portion > principal:
            reduction_portion = principal
            payment = principal + interest_portion
        principal -= reduction_portion
        total_interest += interest_portion
        total_principal += reduction_portion
        if table:
            print(f"{i:5,}  {payment:14,.2f}   {interest_portion:14,.2f}   {reduction_portion:14,.2f}   {principal:14,.2f}")
    return {"#": i, "payment": first_payment, "last payment": payment, "remaining": principal, "total interest": total_interest, "total principal": total_principal}

if __name__ == "__main__":
    main()