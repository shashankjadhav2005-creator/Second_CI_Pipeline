from collections import Counter


def most_frequent(items):
    if not items:
        return None

    counts = Counter(items)
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Most frequent:", most_frequent(numbers))
