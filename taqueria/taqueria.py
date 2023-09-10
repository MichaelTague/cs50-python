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
    x, y = get_fraction("Fraction: ")
    percentage = x / y * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage:.0f}%")

def get_item(prompt):
    while True:
        try:
            item = input(prompt).title()
            if menu[item] != "":
                


            x = int(x)
            y = int(y)
            if y != 0 and x <= y:
                return x, y
        except ValueError:
            pass

main()