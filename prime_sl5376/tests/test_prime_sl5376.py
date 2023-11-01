from prime_sl5376.prime_sl5376 import is_prime
import pandas as pd

def test_is_prime():
    is_prime(12)
    assert ((prime_sl5376.is_prime()).codes == 12).all()
