import emoji

def main():
    sentence = input("Input: ")
    print("Output:", emoji.emojize(sentence, language='alias'))

main()