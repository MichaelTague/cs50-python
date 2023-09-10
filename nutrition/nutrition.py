fruits = {
    "apple": 123,
    "banna": 456,
}

item = input("Item: ").lower()
if item in fruits:
    print(fruits[item])
