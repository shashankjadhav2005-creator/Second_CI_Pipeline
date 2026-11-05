def find_missing_number(nums):
    n = len(nums)
    xor_all = 0

    for i in range(n + 1):
        xor_all = xor_all ^ i

    for num in nums:
        xor_all = xor_all ^ num

    return xor_all


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Missing number:", find_missing_number(numbers))
