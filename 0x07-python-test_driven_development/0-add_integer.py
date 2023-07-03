def factorial(n):
    """Factorial of a number"""
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
