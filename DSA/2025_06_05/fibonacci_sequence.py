# Fibonacci Sequence Implementation
# Multiple approaches: Recursive, Iterative, Dynamic Programming, Matrix Exponentiation

def fibonacci_recursive(n: int) -> int:
    """Recursive approach - O(2^n) time, O(n) space"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n: int) -> int:
    """Iterative approach - O(n) time, O(1) space"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_dp(n: int) -> int:
    """Dynamic Programming approach - O(n) time, O(n) space"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def fibonacci_matrix(n: int) -> int:
    """Matrix exponentiation approach - O(log n) time, O(1) space"""
    if n <= 1:
        return n
    
    def matrix_multiply(a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]
    
    def matrix_power(matrix, power):
        if power == 0:
            return [[1, 0], [0, 1]]
        if power == 1:
            return matrix
        
        half = matrix_power(matrix, power // 2)
        squared = matrix_multiply(half, half)
        
        if power % 2 == 0:
            return squared
        else:
            return matrix_multiply(squared, matrix)
    
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n - 1)
    return result_matrix[0][0]

def fibonacci_generator():
    """Generator for infinite Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage and testing
if __name__ == "__main__":
    # Test different approaches
    test_cases = [0, 1, 5, 10, 20]
    
    print("Fibonacci Sequence Solutions:")
    print("=" * 50)
    
    for n in test_cases:
        print(f"F({n}):")
        print(f"  Recursive: {fibonacci_recursive(n)}")
        print(f"  Iterative: {fibonacci_iterative(n)}")
        print(f"  DP: {fibonacci_dp(n)}")
        print(f"  Matrix: {fibonacci_matrix(n)}")
        print()
    
    # Generate first 15 Fibonacci numbers using generator
    print("First 15 Fibonacci numbers using generator:")
    fib_gen = fibonacci_generator()
    for i in range(15):
        print(f"F({i}) = {next(fib_gen)}")
    
    # Performance comparison for larger numbers
    print("\nPerformance comparison for F(35):")
    import time
    
    start = time.time()
    result = fibonacci_iterative(35)
    end = time.time()
    print(f"Iterative: {result} (Time: {end - start:.6f}s)")
    
    start = time.time()
    result = fibonacci_dp(35)
    end = time.time()
    print(f"DP: {result} (Time: {end - start:.6f}s)")
    
    start = time.time()
    result = fibonacci_matrix(35)
    end = time.time()
    print(f"Matrix: {result} (Time: {end - start:.6f}s)") 