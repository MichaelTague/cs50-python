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
    y, m, d = get_date("Date: ")
    print(f"{y:04}-{m:02}-{d:02}")

def get_date(prompt):
    while True:
        try:
            date = input(prompt)
            date = process_date(date)
            if date != None:
                return date
        except EOFError:
            return list

def process_date(date):
    if date.find("/") >= 0:
        m, d, y = date.split("/")
    else:
        m, d, y = date.split(" ")
        if find(d, ",") < 0:
            return None
        d, junk = d.split(",")
        if find(months, m) < 0:
            return None
        m = find(months, m)
    try:
        y = int(y)
        m = int(m)
        d = int(d)
    except ValueError:
        return None
    if y < 1000 or y > 9999:
        return None
    if m < 1 or m > 12:
        return None
    if d < 1 or d > 31:
        return None
    return [y, m, d]

def find(list, key):
    try:
        return list.index(key)
    except AttributeError:
        return -1

main()