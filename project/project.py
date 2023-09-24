def main():
    amount = 

def payment(amount, interest, term):
    # P = a ÷ { [ (1 + r) n ] - 1 } ÷ [ r (1 + r) n]
    rate = interest/1200
    payment = rate * amount / (1 - (1 + rate)** (-term))


if __name__ == "__main__":
    main()