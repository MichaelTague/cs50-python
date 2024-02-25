def main():
    list = get_list()
    for k, v in sorted(list.items()):
        print(v, k)


def get_list():
    list = {}
    while True:
        try:
            item = input().upper()
            list[item] = list.get(item, 0) + 1
        except EOFError:
            return list

main()