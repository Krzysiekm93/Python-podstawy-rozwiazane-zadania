def factorial(n: int) -> int:
    """This function is counting the factorial for given `n` value"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(6))

