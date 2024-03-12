def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """

    # Base case: 0 or 1
    if n == 0 or n == 1:
        return n
    # Recursive case
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 1) # Fault here

def main():
    n = 10
    print("The 10th Fibonacci number (recursive):", fibonacci_recursive(n))

if __name__ == "__main__":
    main()
