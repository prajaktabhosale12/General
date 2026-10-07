import sys


def fibonacci(n):
    """Yield the first n Fibonacci numbers lazily, using O(1) memory."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    try:
        n = int(input("Enter the number of terms: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Python 3.11+ caps int-to-str conversion at 4300 digits; large terms exceed it.
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)

    # Stream each term to stdout instead of building the whole series in memory.
    write = sys.stdout.write
    write("Fibonacci series:")
    for x in fibonacci(n):
        write(" ")
        write(str(x))
    write("\n")


if __name__ == "__main__":
    main()
