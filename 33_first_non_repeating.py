from collections import Counter


def first_non_repeating(s):
    counts = Counter(s)

    for char in s:
        if counts[char] == 1:
            return char

    return None


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("First non-repeating character:", first_non_repeating(text))
