menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.00
    while True:
        item = get_item("Item: ")
        print(">>>>> Item: ", item)
        if item == None:
            break

        total = total + menu[item]
        print(f"Total: {total:.2f}")

def get_item(prompt):
    while True:
        try:
            item = input(prompt).title()
            if menu[item]:
                return menu[item]
        except EOFError:
            return None
        except ValueError:
            pass

main()