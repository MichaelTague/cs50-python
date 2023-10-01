import re
import sys
import math
import decimal
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN
from scipy import optimize

ONE_CENT = Decimal("0.01").quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
ZERO_CENTS = Decimal("0.00").quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
MAX_TERM = int(1000000000)

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
    interest_annual = str(rounding(interest * 1200)).rstrip('0').rstrip('.')
    term_pretty = pretty_term(term)
    print()
    print(f"Loan Principal: ${principal:,.2f}")
    print(f"Loan Interest:  {interest_annual}%")
    print(f"Loan Term:      {term_pretty}")
    print(f"Loan Payment:   ${payment:,.2f}")
    final = final_payment(principal, interest, term, payment)
    balloon = final['remaining'] + final['last payment']
    print(f"Final Payment:  ${balloon:,.2f}", end="")
    if final['#'] != term:
            print(f" on payment #{final['#']} ({term - final['#']} short of full term)", end="")
    if final['remaining'] != ZERO_CENTS:
        print(f" (a balloon payment which includes ${final['remaining']:,.2f} of remaining principal)", end="")
    print()
    if principal != ZERO_CENTS:
        percent_interest = rounding(final['total interest'] * 100 / (principal + final['total interest']), ROUND_HALF_UP, 0)
    else:
        percent_interest = rounding(ZERO_CENTS, ROUND_DOWN, 0)
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
    if interest != ZERO_CENTS:
        principal: Decimal = payment * (1 - (1 + interest)**(-term)) / interest
    else:
        principal: Decimal = payment * term
    principal = rounding(principal, ROUND_DOWN)
    new_principal = adjust_principal(principal, interest, term, payment)
    if principal != new_principal:
        print("adjust_principal:", principal, new_principal)
    return new_principal

def calc_interest(principal: Decimal, term: int, payment: Decimal) -> Decimal:
    interest = float(0.006) # 6% guess, then use Newton's method to find the a better guess
    interest = optimize.newton(lambda x: float(calc_unrounded_payment(principal, Decimal(x), term) - payment), interest)
    interest = Decimal(interest)
    interest = rounding(Decimal(interest) * Decimal(1200)) / Decimal(1200)
    new_interest = adjust_interest(principal, interest, term, payment)
    if interest != new_interest:
        print('Adjust Interest, old, new:', interest, new_interest)
    return interest

def calc_term(principal: Decimal, interest: Decimal, payment: Decimal) -> Decimal:
    final = final_payment(principal, interest, MAX_TERM, payment)
    return int(final['#'])

def calc_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    payment = calc_unrounded_payment(principal, interest, term)
    payment = rounding(payment, ROUND_UP)
    new_payment = adjust_payment(principal, interest, term, payment)
    if payment != new_payment:
        print('Adjust Paymnet, old, new:', payment, new_payment)
    return new_payment

def calc_unrounded_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    if interest != ZERO_CENTS:
        payment: Decimal = interest * principal / (1 - (1 + interest)**(-term))
    else:
        payment: Decimal = principal / term
    return payment

def adjust_principal(principal: Decimal, interest: Decimal, term: int, payment: Decimal):
    final = final_payment(principal, interest, term, payment)
    if final['#'] == 0:
        return principal
    if final['#'] == term and final['remaining'] == ZERO_CENTS:
        new_principal = principal
        while True:
            old_principal = new_principal
            new_principal += ONE_CENT
            new_final = final_payment(new_principal, interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_principal
    if final['remaining'] != ZERO_CENTS:
        new_principal = principal
        while True:
            new_principal -= ONE_CENT
            new_final = final_payment(new_principal, interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return new_principal
    if final['#'] != term:
        new_principal = principal
        while True:
            old_principal = new_principal
            new_principal += ONE_CENT
            new_final = final_payment(new_principal, interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_principal
    return principal

def adjust_interest(principal: Decimal, interest: Decimal, term: int, payment: Decimal):
    final = final_payment(principal, interest, term, payment)
    if final['#'] == 0:
        return interest
    annual_interest = rounding(interest * Decimal(1200))
    if final['#'] == term and final['remaining'] == ZERO_CENTS:
        interest_add = ZERO_CENTS
        new_interest = annual_interest / Decimal(1200)
        while True:
            old_interest = new_interest
            interest_add -= ONE_CENT
            new_interest = (annual_interest + interest_add) / Decimal(1200)
            new_final = final_payment(principal, new_interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS or new_final['#'] != term:
                return old_interest
    if final['remaining'] != ZERO_CENTS:
        interest_add = ZERO_CENTS
        new_interest = annual_interest / Decimal(1200)
        while True:
            interest_add += ONE_CENT
            new_interest = (annual_interest + interest_add) / Decimal(1200)
            new_final = final_payment(principal, new_interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return new_interest
    if final['#'] != term:
        interest_add = ZERO_CENTS
        new_interest = annual_interest / Decimal(1200)
        while True:
            old_interest = new_interest
            interest_add += ONE_CENT
            new_interest = (annual_interest + interest_add) / Decimal(1200)
            new_final = final_payment(principal, new_interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_interest
    return interest

def adjust_payment(principal: Decimal, interest: Decimal, term: int, payment: Decimal):
    final = final_payment(principal, interest, term, payment)
    if final['#'] == 0:
        return payment
    if final['#'] == term and final['remaining'] == ZERO_CENTS:
        new_payment = payment
        while True:
            old_payment = new_payment
            new_payment -= ONE_CENT
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_payment
    if final['remaining'] != ZERO_CENTS:
        new_payment = payment
        while True:
            new_payment += rounding(ONE_CENT)
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] == ZERO_CENTS:
                return new_payment
    if final['#'] != term:
        new_payment = payment
        while True:
            old_payment = new_payment
            new_payment -= ONE_CENT
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_payment
    return payment

def final_payment(principal: Decimal, interest: Decimal, term: int, payment: Decimal, table=False):
    if principal < payment:
        payment = principal
    first_payment = payment
    total_interest = ZERO_CENTS
    total_principal = ZERO_CENTS
    i = 0
    if table:
        print(f"{0:5,}                                                     {principal:14,.2f}")
    for i in range(1, term + 1):
        if principal == ZERO_CENTS:
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