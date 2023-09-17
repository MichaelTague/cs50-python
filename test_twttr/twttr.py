import sys

def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    result = ""
    for c in word:
        cl = c.lower()
        match cl:
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _ if 'a' <= cl <= 'z' or 'A' <= cl <= 'Z':
                result += c
            case  _:
                sys.exit(1)
    return result

if __name__ == "__main__":
    main()