import re
import sys
import math
import decimal
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN
from scipy import optimize

ctx = decimal.getcontext()
ctx.rounding = ROUND_HALF_UP
#print(decimal.getcontext())

def rounding(value: Decimal, type=ROUND_HALF_UP, digits=2) -> Decimal:
    return value.quantize(Decimal('0.' + '0' * digits), rounding=type)

def main():
    print("Loan Calculations")
    print("If one of the following four is left empty, it will be calculated")
    principal_str = input("        Principal Amount: ")
    interest_str  = input("      Interest per Annum: ")
    term_str      = input("Term in Years and months: ")
    payment_str   = input("  Monthly Payment Amount: ")
    print()

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
    interest_annual = interest * 1200
    interest_annual = interest_annual.normalize()
    term_pretty = pretty_term(term)
    print()
    print(f"Loan Principal: ${principal:,.2f}")
    print(f"Loan Interest:  {interest_annual:0,f}%")
    print(f"Loan Term:      {term_pretty}")
    print(f"Loan Payment:   ${payment:,.2f}")
    final = final_payment(principal, interest, term, payment)
    balloon = final['remaining'] + final['last payment']
    print(f"Final Payment:  ${balloon:,.2f}", end="")
    if final['#'] != term:
            print(f" on payment #{final['#']} ({term - final['#']} short of full term)", end="")
    if final['remaining'] != Decimal(0):
        print(f" (a balloon payment which includes ${final['remaining']:,.2f} of remaining principal)", end="")
    print()
    if principal != Decimal(0):
        percent_interest = rounding(final['total interest'] * 100 / (principal + final['total interest']), ROUND_HALF_UP, 0)
    else:
        percent_interest = Decimal(0)
    percent_interest = percent_interest.normalize()
    print(f"Total Interest: ${final['total interest']:,.2f} ({percent_interest}% of payments)")

def pretty_term(term: int):
    years = term // 12
    months = term % 12
    if years == 0:
        term = str(months) + " Month"
        if months != 1:
            term += "s"
        return term
    term = str(years) + " Year"
    if years != 1:
        term += "s"
    if months == 0:
        return term
    term += ", " + str(months) + " Month"
    if months != 1:
        term += "s"
    return term

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
        sys.exit("Term must not be negative, looks like: 30 yrs; 60 months; 3 years, 6 months")
    if provided < 3:
        sys.exit("Only one of Principal, Interest, Term, and Payment may be left empty")
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
    if term < 0:
        raise ValueError("Negative term")
    return term

def calc_principal(interest: Decimal, term: int, payment: Decimal) -> Decimal:
    if interest != Decimal(0):
        principal: Decimal = payment * (1 - (1 + interest)**(-term)) / interest
    else:
        principal: Decimal = payment * term
    return rounding(principal, ROUND_DOWN)

def calc_interest(principal: Decimal, term: int, payment: Decimal) -> Decimal:
    interest = float(0.006) # 6% guess, then use Newton's method to find the a better guess
    interest = optimize.newton(lambda x: float(calc_unrounded_payment(principal, Decimal(x), term) - payment), interest)
    interest = Decimal(interest)
    return rounding(interest, ROUND_HALF_UP)

def calc_term(principal: Decimal, interest: Decimal, payment: Decimal) -> Decimal:
    if interest != Decimal(0):
        term = - math.log(1 - (principal * interest / payment)) / math.log(1 + interest)
    else:
        term = principal / payment
    return int(rounding(term, ROUND_UP, 0))

def calc_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    payment = calc_unrounded_payment(principal, interest, term)
    payment = rounding(payment, ROUND_UP)
    print("calc_payment payment", len(str(payment)), payment)
    new_payment = adjust_payment_for_final(principal, interest, payment, term)
    if payment != new_payment:
        print('Adjust Paymnet, old, new:', payment, new_payment)
    return new_payment

def adjust_payment_for_final(principal: Decimal, interest: Decimal, payment: Decimal, term: int):
    final = final_payment(principal, interest, term, payment)
    if final['#'] == 0:
        return payment
    if final['#'] == term and final['remaining'] == Decimal(0):
        new_payment = payment
        while True:
            old_payment = new_payment
            new_payment -= Decimal(0.01)
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] != Decimal(0):
                return old_payment
    if final['remaining'] != Decimal(0):
        new_payment = payment
        while True:
            new_payment += Decimal(0.01)
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] == Decimal(0):
                return new_payment
    if final['#'] != term:
        new_payment = payment
        while True:
            old_payment = new_payment
            new_payment -= Decimal(0.01)
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] != Decimal(0):
                return old_payment
    return payment

def calc_unrounded_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    if interest != Decimal(0):
        payment: Decimal = interest * principal / (1 - (1 + interest)**(-term))
    else:
        payment: Decimal = principal / term
    return payment

def final_payment(principal: Decimal, interest: Decimal, term: int, payment: Decimal, table=False):
    print("final_payment payment", len(str(payment)), payment)
    if principal < payment:
        payment = principal
    first_payment = payment
    total_interest = Decimal(0)
    total_principal = Decimal(0)
    i = 0
    if table:
        print(f"{0:5,}                                                     {principal:14,.2f}")
    for i in range(1, term + 1):
        if principal == Decimal(0):
            i -= 1
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