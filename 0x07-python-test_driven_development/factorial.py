def factorial(n):
    """Factorial of a number

    >>> factorial(2)
    2   
    >>> factorial(0)
    1   
    >>> factorial(-1)
    >>> factorial(ff)
    Traceback (most recent call last):   
    ...
    NameError: name 'ff' is not defined
    >>> factorial(12)
    479001600
    """
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()