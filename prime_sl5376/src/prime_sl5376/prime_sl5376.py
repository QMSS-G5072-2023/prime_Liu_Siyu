import pandas as pd
import math

def is_prime(n):
    """
    Purpose
    ----------
    The purpose of this function is to check whether the interger n is a prime number

    Inputs 
    ------
    The input is the integer n.

    Outputs
    -------
    If input smaller than 1, the output of this function will be False.
    If input is larger than 1, this function will checak whether this number is a prime number.
    The output will be True if the number is a prime number, and will be False if it isn't.

    Examples
    -------
    >>> from prime_sl5376 import prime_sl5376
    >>> n = 12
    >>> prime_sl5376.is_prime(12)
    >>> False
    """

    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
