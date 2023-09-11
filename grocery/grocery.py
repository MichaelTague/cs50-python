def main():
    list = get_list()
    print(list.sort())

def get_list():
    list = {}
    while True:
        try:
            item = input()
            list[item] = list.get(item, 0) + 1
        except EOFError:
            return None

main()