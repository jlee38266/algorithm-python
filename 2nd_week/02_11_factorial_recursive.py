def factorial(n):
    for i in range(n):
        if n == 1:
            return 1

    return n * factorial(n - 1)

print(factorial(5))
