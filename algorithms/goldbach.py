def is_prime(num):
    """Returns True if the number is prime, otherwise False."""
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def goldbach(n):
    """Returns all prime pairs whose sum equals the given even number."""
    if n <= 2 or n % 2 != 0:
        return []

    pairs = []

    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            pairs.append((i, n - i))

    return pairs


def main():
    while True:
        try:
            num = int(input("Enter an even number greater than 2: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    pairs = goldbach(num)

    if pairs:
        print(f"\nGoldbach pairs for {num}:")
        print("-" * 30)

        for a, b in pairs:
            print(f"{a} + {b} = {num}")

    else:
        print("Error: Please enter an even number greater than 2.")


if __name__ == "__main__":
    main()
