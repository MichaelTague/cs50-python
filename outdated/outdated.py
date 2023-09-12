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
    print(get_date("Date: "))

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
        if d.find(",") < 0:
            return None
        d, junk = d.split(",")
        if months.find(m) < 0:
            return None
        m = months.find(m)
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

main()