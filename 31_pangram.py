import string


def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(s.lower()))


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Is pangram:", is_pangram(text))
