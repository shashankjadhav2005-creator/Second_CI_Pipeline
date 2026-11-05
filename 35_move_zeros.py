def move_zeros(numbers):
    non_zeros = [x for x in numbers if x != 0]
    zeros = [0] * (len(numbers) - len(non_zeros))

    return non_zeros + zeros


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Original:", numbers)
    print("Zeros moved:", move_zeros(numbers))
