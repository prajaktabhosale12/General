def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    try:
        n = int(input("Enter the number of terms: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n <= 0:
        print("Please enter a positive integer.")
        return

    print("Fibonacci series:", " ".join(str(x) for x in fibonacci(n)))


if __name__ == "__main__":
    main()
