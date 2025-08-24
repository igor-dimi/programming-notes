def f(n):
    """returns the input

    >>> f(1)
    1
    >>> f(2)
    2
    """
    return n

if __name__ == "__main__":
    print("I am the main program")
    import doctest
    doctest.testmod(verbose=True)  # verbose helps you see what's run
