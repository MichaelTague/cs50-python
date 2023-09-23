import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.search(r"https://www.youtube.com/embed/([].+)\"", s):
        return "https://youtu.be/{match[1]}"
    return None

if __name__ == "__main__":
    main()
