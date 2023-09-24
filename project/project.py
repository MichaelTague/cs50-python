import math
INT_ROUND_DECIMAL_DIGITS=6

def main():
    amount = float(input("Amount: "))
    interest = float(input("Interest per annum: "))
    rate = interest / 1200 #round(interest / 1200, INT_ROUND_DECIMAL_DIGITS)
    term = int(input("Term (in months): "))
    payment = calc_payment(amount, rate, term)
    print(f"Monthly payment: {payment:.2f}")
    final_payment(amount, rate, term, payment)

def calc_payment(amount: float, rate: float, term: int) -> float:
    payment = rate * amount / (1 - (1 + rate)**(-term))
    print(payment)
    return math.ceil(payment * 100) / 100

def final_payment(amount, rate, term, payment):
    total_interest = 0
    
    for i in range(1, term + 1):
        interest_portion = round(amount * rate, 2)
        reduction_portion = payment - interest_portion
        if reduction_portion > amount:
            reduction_portion = amount
            payment = amount + interest_portion
        amount -= reduction_portion
#        print(f"{i:3}  {payment:9.2f}   {interest_portion:9.2f}   {reduction_portion:9.2f}   {amount:9.2f}")
    return i, payment,

if __name__ == "__main__":
    main()