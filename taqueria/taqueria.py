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
        amount = get_item("Item: ")
        if amount == None:
            break
        total = total + amount
        print(f"Total: ${total:.2f}")

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
        except KeyError:
            pass

main()