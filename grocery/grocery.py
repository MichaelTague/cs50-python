list = {}

def main():



def get_list():
    while True:
        item = input()
        list[item] = list.get(item, 0) + 1
        
        if item in list:
            value = list[item] + 1



main()