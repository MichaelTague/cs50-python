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
            case _:
                result += c
    return result

if __name__ == "__main__":
    main()