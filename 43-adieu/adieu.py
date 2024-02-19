import inflect

p = inflect.engine()

def main():
    names = get_list("Name: ")
    printable_names = p.join(names)
    print("Adieu, adieu, to", printable_names)

def get_list(prompt):
    list = []
    while True:
        try:
            item = input(prompt)
            list.append(item)
        except EOFError:
            return list

main()