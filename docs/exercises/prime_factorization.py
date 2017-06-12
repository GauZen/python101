r"""
The `prime factor`_\ s of 360 are

.. math::

    360 = 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 \cdot 5 = 2^3 \cdot 3^2 \cdot 5.

Write a function that returns a dictionary whose first keys correspond to the
prime factor and the value to the multiplicity of this prime factor. For
example, given 360 the function should return::

    {
        2: 3,
        3: 2,
        5: 1
    }

.. autofunction:: prime_factorization

Start by downloading the
:exercise:`exercise template </exercises/prime_factorization.py>` and editing
this file. You can run tests via

.. code-block:: console

    $ python prime_factorization.py test

to check whether you got a correct solution. You can also take a look at
:solution:`one possible solution </exercises/prime_factorization.py>`.

.. _prime factor: https://en.wikipedia.org/wiki/Prime_factor

"""


def prime_factorization(n):
    """Return the prime factorization of `n`.

    Parameters
    ----------
    n : int
        The number for which the prime factorization should be computed.

    Returns
    -------
    dict[int, int]
        List of tuples containing the prime factors and multiplicities of `n`.

    """
    # begin solution
    prime_factors = {}

    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n /= i
            try:
                prime_factors[i] += 1
            except KeyError:
                prime_factors[i] = 1

    if n > 1:
        try:
            prime_factors[n] += 1
        except KeyError:
            prime_factors[n] = 1
    return prime_factors
    # end solution

# -----------------------------------------------------------------------------
# In the following the tests for this exercise are given---do not modify them.
import sys
import pytest


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (1, {}),
        (2, {2: 1}),
        (3, {3: 1}),
        (4, {2: 2}),
        (5, {5: 1}),
        (6, {2: 1, 3: 1}),
        (7, {7: 1}),
        (8, {2: 3}),
        (9, {3: 2}),
        (360, {2: 3, 3: 2, 5: 1})
    ])
def test_correct_result(n, expected):
    assert prime_factorization(n) == expected


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[-1] == 'test':
        pytest.main([__file__])
