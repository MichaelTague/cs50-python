months = [
    None,
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    print(months.index("May"))
    exit()
    list = get_list()
    for k, v in sorted(list.items()):
        print(v, k)


def get_date(prompt):
    while True:
        try:
            item = input(prompt)
            list[item] = list.get(item, 0) + 1
        except EOFError:
            return list

def is_valid_date(date):
    pass


main()