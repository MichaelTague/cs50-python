amount = 50
while amount != 0:
    print("Amount Due:", amount)
    coin = input("Input Coin: ")
    match coin:
        case "25" | "10" | "5":
            amount = amount - int(coin)
