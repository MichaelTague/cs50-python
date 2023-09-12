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


def get_date(prompt):
    while True:
        try:
            item = input(prompt)
            list[item] = list.get(item, 0) + 1
        except EOFError:
            return list

def process_date(date):
    if date.find("/") >= 0:
        m, d, y = date.split("/")
    else:
        m, d, y = date.split(" ")
        if d.find(",") < 0:
            return None
        d, junk = d.split(",")
        if months.find(m) < 0:
            return None



    pass


main()