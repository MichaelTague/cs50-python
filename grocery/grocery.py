list = {}

def main():
    


def get_list():
    while True:
        try:
            item = input()
            list[item] = list.get(item, 0) + 1
        except EOFError:
            return None

main()