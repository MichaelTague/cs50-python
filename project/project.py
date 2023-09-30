import re
import sys
import math
import decimal
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN
from scipy import optimize

ctx = decimal.getcontext()
ctx.rounding = ROUND_HALF_UP
#print(decimal.getcontext())


def rounding(value: Decimal, round_type=ROUND_DOWN) -> Decimal:
    return value.quantize(Decimal('0.00'), rounding=round_type)

def main():
    print("Input three answers for the following four questions, the empty answer will be calaulated.")
    principal_str = input("Principal Amount: ")
    interest_str = input("Interest per Annum: ")
    term_str = input("Term in Years (or write \"months\"): ")
    payment_str = input("Monthly Payment: ")

    principal, interest, term, payment = convert_input(principal_str, interest_str, term_str, payment_str)

    if principal == None:
        principal = calc_principal(interest, term, payment)
    elif interest == None:
        interest: float = calc_interest(principal, term, payment)
    elif term == None:
        term = calc_term(principal, interest, payment)
    elif payment == None:
        payment = calc_payment(principal, interest, term)
    print_loan(principal, interest, term, payment)

def print_loan(principal: Decimal, interest: Decimal, term: int, payment: Decimal):
    interest *= 1200
    term = pretty_term(term)
    print(f"Loan Principal: ${principal:,.2f}")
    if interest == interest.to_integral():
        print(f"Loan Interest:  {int(interest):,f}%")
    else:
        print(f"Loan Interest:  {interest:,.2f}%")
    print(f"Loan Term:      {term}")
    print(f"Loan Payment:   ${payment:,.2f}")

def pretty_term(term: int):
    years = term // 12
    months = term % 12
    if years == 0:
        return str(term) + " Months"
    if months == 0:
        return str(years) + " Years"
    return str(years) + " Years, " + str(months) + " Months"

def convert_input(principal_str, interest_str, term_str, payment_str):
    provided = 0
    principal = interest = term = payment = None
    try:
        if principal_str != "":
            principal = Decimal(principal_str)
            provided += 1
        if interest_str != "":
            interest = Decimal(interest_str) / Decimal(1200)
            provided += 1
        if term_str != "":
            term = parse_term_str(term_str)
            provided += 1
        if payment_str != "":
            payment = Decimal(payment_str)
            provided += 1
    except decimal.InvalidOperation:
        sys.exit("Principal, Interest, and Payment must be Integer or Decimal Number")
    except ValueError:
        sys.exit("Term must be greater than zero and similar to these:  30 yrs; 60 months; 3 years, 6 months")
    if provided != 3:
        sys.exit("One, and only one, of Principal, Interest, Term, and Payment should be left empty")
    return principal, interest, term, payment

def parse_term_str(term_str: str):
    years: int = 0
    months: int = 0
    matches = re.findall(r'(\d+)\s*(\w+)?', term_str)
    for match in matches:
        number, unit = match
        if unit == "":
            years = int(number)
        elif re.search(r'(yr|year)s?', unit, re.IGNORECASE):
            years = int(number)
        elif re.search(r'(mo|month)s?', unit, re.IGNORECASE):
            months = int(number)
        else:
            raise ValueError("Invalid Term format")
    term: int = years * 12 + months
    if term <= 0:
        raise ValueError("Zero term")
    return term

def print_final_payment(d: dict):
    term = d["#"]
    last = d["last payment"]
    total_interest = d["total interest"]
    total_principal = d["total principal"]
    total_payments = total_interest + total_principal
    remaining = d["remaining"]
    print(f"Last payment: ${last:,.2f} at payment: {term:,}, total interest: ${total_interest:,.2f}, total payments: ${total_payments:,.2f}, balloon (if any): ${remaining:,.2f}")

def calc_principal(interest: Decimal, term: int, payment: Decimal) -> Decimal:
    principal: Decimal = payment * (1 - (1 + interest)**(-term)) / interest
    return rounding(principal, ROUND_UP)

def calc_interest(principal: Decimal, term: int, payment: Decimal) -> Decimal:
    interest = float(0.006) # 6% guess, then use Newton's method to find the a better guess
    interest = optimize.newton(lambda x: float(calc_unrounded_payment(principal, Decimal(x), term) - payment), interest)
    interest = Decimal(interest)
    return rounding(interest, ROUND_HALF_UP)

def calc_term(principal: Decimal, interest: Decimal, payment: Decimal) -> Decimal:
    term = - math.log(1 - (principal * interest / payment)) / math.log(1 + interest)
    return rounding(term, ROUND_DOWN)

def calc_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    payment = calc_unrounded_payment(principal, interest, term)
    payment = rounding(payment, ROUND_UP)
    payment = adjust_payment_for_final(principal, interest, payment, term)
    return payment

def adjust_payment_for_final(principal: Decimal, interest: Decimal, payment: Decimal, term: int):
    return payment

def calc_unrounded_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    payment: Decimal = interest * principal / (1 - (1 + interest)**(-term))
    print(interest, payment)
    return Decimal(payment)

def final_payment(principal: Decimal, interest: Decimal, term: int, payment: Decimal, table=False):
    first_payment = payment
    total_interest = Decimal(0)
    total_principal = Decimal(0)
    if table:
        print(f"{0:5,}                                                     {principal:14,.2f}")
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