import emoji

def main():
    while True:
        try:
            sentence = input("Input: ")
            print(emoji.emojize(sentence))
        except EOFError:
            return

main()