def main():

def shorten(word):


if 




string = input("Input: ")
for c in string:
    cl = c.lower()
    match cl:
        case "a" | "e" | "i" | "o" | "u":
            continue
        case _:
            print(c, end="")
print()