def rotate_string(s, k):
    if not s:
        return ""

    n = len(s)
    k = k % n

    if k == 0:
        return s

    return s[-k:] + s[:-k]


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter rotation positions: "))
    print("Rotated string:", rotate_string(text, k))
