def nearst_square(n):
    """Function finds the nearst square of a number
    n-> number as input
    return the square root of number which is less or equal
    """
    root = 0
    while (root + 1) ** 2 <= n:
        root += 1
    return root ** 2

                                               