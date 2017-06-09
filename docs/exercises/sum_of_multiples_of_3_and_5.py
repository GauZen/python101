"""
.. note::

    The following problem was inspired by `Problem 1 at Project Euler`_.

If you list all the natural numbers below 10 that are multiples of 3 or 5, you
get 3, 5, 6, and 9. The sum of these multiples is 23. Define a function
according to the following definition:

.. autofunction:: sum_of_multiples_of_3_and_5

Start by downloading the
:exercise:`exercise template </exercises/sum_of_multiples_of_3_and_5.py>` and
editing this file. You can run tests via

.. code-block:: console

    $ python sum_of_multiples_of_3_and_5.py test

to check whether you got a correct solution. You can also take a look at
:solution:`one possible solution </exercises/sum_of_multiples_of_3_and_5.py>`.

.. _Problem 1 at Project Euler: https://projecteuler.net/problem=1

"""


def sum_of_multiples_of_3_and_5(n):
    """Return the sum of all multiples of 3 and 5 below `n`.

    Parameters
    ----------
    n : int
        The number up to which the sum of multiples of 3 and 5 is computed.

    Returns
    -------
    int
        The sum of all multiples of 3 and 5 up to `n`.

    """
    # begin solution
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s
    # end solution

# -----------------------------------------------------------------------------
# In the following the tests for this exercise are given---do not modify them.
import sys
import pytest


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 3),
        (5, 3),
        (6, 8),
        (7, 14),
        (8, 14),
        (9, 14),
        (10, 23)
    ])
def test_correct_result(n, expected):
    assert sum_of_multiples_of_3_and_5(n) == expected


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[-1] == 'test':
        pytest.main([__file__])
