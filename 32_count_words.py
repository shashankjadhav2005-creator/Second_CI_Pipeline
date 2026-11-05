def count_words(sentence):
    if not sentence or not sentence.strip():
        return 0

    return len(sentence.split())


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Word count:", count_words(text))
