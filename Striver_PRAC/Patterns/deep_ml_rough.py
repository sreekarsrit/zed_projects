def first_n_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fibo = [0, 1]
    a, b = 0, 1
    
    for _ in range(2, n):
        a, b = b, a + b
        fibo.append(b)

    return fibo

# Example run
print(first_n_fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(first_n_fibonacci(0))  # Output: []