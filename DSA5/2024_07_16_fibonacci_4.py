def fibonacci(n):
    """
    Calculate nth Fibonacci number using dynamic programming.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test
if __name__ == "__main__":
    print(fibonacci(10))  # 55
