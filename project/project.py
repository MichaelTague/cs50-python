import re
import sys
import math
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP, ROUND_DOWN
from scipy import optimize

DEBUG: bool             = False
DEBUG_FINAL: bool       = False

ONE_CENT: Decimal       = Decimal("0.01").quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
ZERO_CENTS: Decimal     = Decimal("0.00").quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
MAX_TERM: int           = int(1000000000)
TWELVE_HUNDRED: Decimal = Decimal("1200")
EMPTY: Decimal          = Decimal("-1")
RED: str                = "\033[91m"
BLUE: str               = "\033[94m"
LIGHT_BLUE: str         = "\033[96m"
GREEN: str              = "\033[92m"
COLOR_END: str          = "\033[0m"

def rounding(value: Decimal, type: str = ROUND_HALF_UP, digits: int = 2) -> Decimal:
    return value.quantize(Decimal('0.' + '0' * digits), rounding=type)

def red(string: str) -> str:
    return RED + string + COLOR_END

def main():
    print(GREEN + "Loan Calculations.  Enter 3 or 4 of the following:" + COLOR_END)
    principal_str = input("        Principal Amount: ")
    interest_str  = input("      Interest per Annum: ")
    term_str      = input("Term in Years and Months: ")
    payment_str   = input("  Monthly Payment Amount: ")
    if DEBUG: print()

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
    response = input("Amortization Table (Y/N)? ").lower()
    if response in ["yes", "y"]:
        final_payment(principal, interest, term, payment, True)
    if DEBUG: print()

def print_loan(principal: Decimal, interest: Decimal, term: int, payment: Decimal) -> None:
    interest_annual: str = str(rounding(interest * TWELVE_HUNDRED)).rstrip('0').rstrip('.')
    term_pretty: str = pretty_term(term)
    print()
    print(f"          Loan Principal: ${principal:,.2f}")
    print(f"          Loan Interest:  {interest_annual}%")
    print(f"          Loan Term:      {term_pretty}")
    print(f"          Loan Payment:   ${payment:,.2f}")
    final = final_payment(principal, interest, term, payment)
    balloon = final['remaining'] + final['last payment']
    print(f"          Final Payment:  ${balloon:,.2f}", end="")
    if final['#'] != term:
            print(f" on payment #{final['#']} ({term - final['#']} short of full term)", end="")
    if final['remaining'] != ZERO_CENTS:
        print(f" (a balloon payment which includes ${final['remaining']:,.2f} of remaining principal)", end="")
    print()
    if principal != ZERO_CENTS:
        percent_interest = rounding(final['total interest'] * 100 / (principal + final['total interest']), ROUND_HALF_UP, 0)
    else:
        percent_interest = rounding(ZERO_CENTS, ROUND_DOWN, 0)
    print(f"          Total Interest: ${final['total interest']:,.2f} ({percent_interest}% of payments)")

def pretty_term(term: int) -> str:
    years = term // 12
    months = term % 12
    if years == 0:
        term_str = str(months) + " Month"
        if months != 1:
            term_str += "s"
        return term_str
    term_str = str(years) + " Year"
    if years != 1:
        term_str += "s"
    if months == 0:
        return term_str
    term_str += ", " + str(months) + " Month"
    if months != 1:
        term_str += "s"
    return term_str

def convert_input(principal_str: str, interest_str: str, term_str: str, payment_str: str) -> tuple:
    provided: int = 0
    principal: Decimal = None
    interest: Decimal = None
    term: int = None
    payment: Decimal = None
    try:
        if principal_str != "":
            principal = Decimal(principal_str)
            provided += 1
        if interest_str != "":
            interest = Decimal(interest_str) / TWELVE_HUNDRED
            provided += 1
        if term_str != "":
            term = parse_term_str(term_str)
            provided += 1
        if payment_str != "":
            payment = Decimal(payment_str)
            provided += 1
    except decimal.InvalidOperation:
        sys.exit(red("Principal, Interest, and Payment must be Integer or Decimal Number"))
    except ValueError:
        sys.exit(red("Term must not be negative, looks like: 30 yrs; 60 months; 3 years, 6 months"))
    if provided < 3:
        sys.exit(red("Only one of Principal, Interest, Term, and Payment may be left empty"))
    if principal != None and principal < ZERO_CENTS:
        sys.exit(red("Principal cannot be negative"))
    if interest != None and interest < ZERO_CENTS:
        sys.exit(red("Interest cannot be negative"))
    if term != None and term < 0:
        sys.exit(red("Term cannot be negative"))
    return principal, interest, term, payment

def parse_term_str(term_str: str) -> int:
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
    new_principal: Decimal = adjust_principal(principal, interest, term, payment)
    if DEBUG and principal != new_principal:
        print(RED + "adjust_principal, principal was adjusted from", principal, "to", new_principal, COLOR_END)
    return new_principal

def calc_interest(principal: Decimal, term: int, payment: Decimal) -> Decimal:
    if principal == ZERO_CENTS or term == 0 or payment == ZERO_CENTS:
        return ZERO_CENTS

    interest = float(0.006) # 6% guess, then use Newton's method to find the a better guess
    interest = optimize.newton(lambda x: float(calc_unrounded_payment(principal, Decimal(x), term) - payment), interest)
    interest = Decimal(interest)
    interest = rounding(Decimal(interest) * TWELVE_HUNDRED) / TWELVE_HUNDRED
    new_interest: Decimal = adjust_interest(principal, interest, term, payment)
    if DEBUG and interest != new_interest:
        print(RED + 'calc_interest, interest was adjusted from', interest, 'to', new_interest, COLOR_END)
    return new_interest

def calc_term(principal: Decimal, interest: Decimal, payment: Decimal) -> Decimal:
    if payment == ZERO_CENTS or principal == ZERO_CENTS or interest == ZERO_CENTS:
        term = 0
    else:
        top = - math.log(float(1 - principal * interest / payment))
        bottom = math.log(float(1 + interest))
        term = math.ceil(top / bottom)
    final = final_payment(principal, interest, MAX_TERM, payment)
    new_term: int = int(final['#'])
    if DEBUG and term != new_term:
        print(RED + 'calc_term, term was adjusted from', term, 'to', new_term, COLOR_END)
    return new_term

def calc_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    payment = calc_unrounded_payment(principal, interest, term)
    payment = rounding(payment, ROUND_UP)
    new_payment: Decimal = adjust_payment(principal, interest, term, payment)
    if DEBUG and payment != new_payment:
        print(RED + 'calc_payment, payment was adjusted from', payment, 'to', new_payment, COLOR_END)
    return new_payment

def calc_unrounded_payment(principal: Decimal, interest: Decimal, term: int) -> Decimal:
    if term == 0:
        return ZERO_CENTS
    if interest == ZERO_CENTS:
        return principal / term
    return interest * principal / (1 - (1 + interest)**(-term))

def adjust_principal(principal: Decimal, interest: Decimal, term: int, payment: Decimal) -> Decimal:
    final = final_payment(principal, interest, term, payment)
    if final['#'] == 0:
        return principal
    if final['#'] == term and final['remaining'] == ZERO_CENTS:
        if DEBUG: print(red("adjust_principal, normal"))
        new_principal = principal
        while True:
            old_principal = new_principal
            new_principal += ONE_CENT
            new_final = final_payment(new_principal, interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_principal
    if final['remaining'] != ZERO_CENTS:
        if DEBUG: print(red("adjust_principal, remaining"))
        new_principal = principal
        while True:
            new_principal -= ONE_CENT
            new_final = final_payment(new_principal, interest, term, payment)
            if new_final['remaining'] == ZERO_CENTS:
                return new_principal
    if final['#'] != term:
        if DEBUG: print(red("adjust_principal, term"))
        new_principal = principal
        while True:
            old_principal = new_principal
            new_principal += ONE_CENT
            new_final = final_payment(new_principal, interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_principal
    return principal

def adjust_interest(principal: Decimal, interest: Decimal, term: int, payment: Decimal) -> Decimal:
    if DEBUG: print(RED + "adjust_interst, starting interest:", rounding(interest * TWELVE_HUNDRED), COLOR_END)
    final = final_payment(principal, interest, term, payment)
    if final['#'] == 0:
        return interest
    annual_interest = rounding(interest * TWELVE_HUNDRED)
    if final['#'] == term and final['remaining'] == ZERO_CENTS:
        if DEBUG: print(red("adjust_interest, normal"))
        interest_add = ZERO_CENTS
        new_interest = annual_interest / TWELVE_HUNDRED
        while True:
            old_interest = new_interest
            interest_add += ONE_CENT
            new_interest = (annual_interest + interest_add) / TWELVE_HUNDRED
            new_final = final_payment(principal, new_interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS or new_final['#'] != term:
                return old_interest
    if final['remaining'] != ZERO_CENTS:
        if DEBUG: print(red("adjust_interest, remaining"))
        interest_add = ZERO_CENTS
        new_interest = annual_interest / TWELVE_HUNDRED
        while True:
            interest_add -= ONE_CENT
            new_interest = (annual_interest + interest_add) / TWELVE_HUNDRED
            new_final = final_payment(principal, new_interest, term, payment)
            if new_final['remaining'] == ZERO_CENTS:
                return new_interest
    if final['#'] != term:
        if DEBUG: print(red("adjust_interest, term"))
        interest_add = ZERO_CENTS
        new_interest = annual_interest / TWELVE_HUNDRED
        while True:
            old_interest = new_interest
            interest_add += ONE_CENT
            new_interest = (annual_interest + interest_add) / TWELVE_HUNDRED
            new_final = final_payment(principal, new_interest, term, payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_interest
    return interest

def adjust_payment(principal: Decimal, interest: Decimal, term: int, payment: Decimal) -> Decimal:
    final = final_payment(principal, interest, term, payment)
    if final['#'] == 0:
        return payment
    if final['#'] == term and final['remaining'] == ZERO_CENTS:
        if DEBUG: print(red("adjust_payment, normal"))
        new_payment = payment
        while True:
            old_payment = new_payment
            new_payment -= ONE_CENT
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_payment
    if final['remaining'] != ZERO_CENTS:
        if DEBUG: print(red("adjust_payment, remaining"))
        new_payment = payment
        while True:
            new_payment += rounding(ONE_CENT)
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] == ZERO_CENTS:
                return new_payment
    if final['#'] != term:
        if DEBUG: print(red("adjust_payment, term"))
        new_payment = payment
        while True:
            old_payment = new_payment
            new_payment -= ONE_CENT
            new_final = final_payment(principal, interest, term, new_payment)
            if new_final['remaining'] != ZERO_CENTS:
                return old_payment
    return payment

def final_payment(principal: Decimal, interest: Decimal, term: int, payment: Decimal, table=False) -> dict:
    if principal < payment:
        payment = principal
    first_payment: Decimal = payment
    total_interest: Decimal = ZERO_CENTS
    total_principal: Decimal = ZERO_CENTS
    i: int = 0
    if table:
        print()
        print("    #         Payment         Interest        Reduction        Principal")
        print(f"{0:5,}     -----------      -----------      -----------   {principal:14,.2f}")
    for i in range(1, term + 1):
        if principal == ZERO_CENTS:
            i -= 1
            break
        interest_portion = rounding(principal * interest, ROUND_HALF_UP)
        if i%12 == 1:
             reduction_portion = payment + 1250 - interest_portion
        else:
            reduction_portion = payment - interest_portion
        if reduction_portion > principal:
            reduction_portion = principal
            payment = principal + interest_portion
        principal -= reduction_portion
        total_interest += interest_portion
        total_principal += reduction_portion
        if table:
            print(f"{i:5,}  {payment:14,.2f}   {interest_portion:14,.2f}   {reduction_portion:14,.2f}   {principal:14,.2f}")
    result: dict = {"#": i, "payment": first_payment, "last payment": payment, "remaining": principal, "total interest": total_interest, "total principal": total_principal}
    if DEBUG_FINAL:
        print(red("final_payment:"), result)
    return result

if __name__ == "__main__":
    main()