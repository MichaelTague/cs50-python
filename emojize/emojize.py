import emoji

def main():
    while True:
        try:
            sentence = input("Input: ")
            print("Output:", emoji.emojize(sentence, language='alias'))
        except EOFError:
            print()
            return

main()